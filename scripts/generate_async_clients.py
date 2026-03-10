#!/usr/bin/env python3
"""
Generate Async*Client files from their sync counterparts.

Each *Client.py in paddle_billing/Resources/ is transformed into an
Async*Client.py with:
  - All class-level methods made `async def`
  - All `self.client._get/post/patch/delete(...)` calls awaited
  - All intra-class method calls awaited
  - Class name prefixed with `Async`
  - TYPE_CHECKING import updated to reference AsyncClient

Usage:
    python scripts/generate_async_clients.py          # generate all
    python scripts/generate_async_clients.py --check  # verify up-to-date (for CI)
"""

import ast
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
RESOURCES_DIR = REPO_ROOT / "paddle_billing" / "Resources"

AUTOGEN_HEADER = """\
# AUTO-GENERATED FILE — DO NOT EDIT DIRECTLY.
# Source: {source_rel}
# Regenerate with: python scripts/generate_async_clients.py
"""


def _class_method_line_numbers(source: str, class_name: str) -> set[int]:
    """Return the 1-based line numbers of all direct method `def` lines on the class (excluding __init__)."""
    tree = ast.parse(source)
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef) and node.name == class_name:
            return {
                child.lineno
                for child in node.body
                if isinstance(child, ast.FunctionDef) and child.name != "__init__"
            }
    return set()


def _class_method_names(source: str, class_name: str) -> set[str]:
    """Return names of all methods defined directly on the class."""
    tree = ast.parse(source)
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef) and node.name == class_name:
            return {
                child.name
                for child in node.body
                if isinstance(child, ast.FunctionDef)
            }
    return set()


def _class_name(source: str) -> str | None:
    tree = ast.parse(source)
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            return node.name
    return None


def transform(source: str, source_rel: str) -> str:
    sync_class = _class_name(source)
    if not sync_class:
        raise ValueError("No class found in source")

    async_class = f"Async{sync_class}"
    method_lines = _class_method_line_numbers(source, sync_class)
    method_names = _class_method_names(source, sync_class) - {"__init__"}

    lines = source.splitlines(keepends=True)
    result = []

    for lineno, line in enumerate(lines, start=1):
        # Make class-level `def` into `async def`
        if lineno in method_lines:
            line = re.sub(r"^(\s*)def ", r"\1async def ", line)

        # Await self.client._get / _post / _patch / _delete calls
        line = re.sub(
            r"\breturn (self\.client\._(?:get|post|patch|delete)\()",
            r"return await \1",
            line,
        )

        # Await intra-class method calls: `return self.method_name(`
        for name in method_names:
            line = re.sub(
                rf"\breturn (self\.{re.escape(name)}\()",
                rf"return await \1",
                line,
            )

        result.append(line)

    output = "".join(result)

    # Rename the class
    output = output.replace(f"class {sync_class}:", f"class {async_class}:")

    # Update TYPE_CHECKING import block
    output = output.replace(
        "from paddle_billing.Client import Client",
        "from paddle_billing.AsyncClient import AsyncClient",
    )

    # Update constructor annotation
    output = output.replace('client: "Client"', 'client: "AsyncClient"')

    return AUTOGEN_HEADER.format(source_rel=source_rel) + output


def find_sync_clients() -> list[Path]:
    clients = []
    for path in sorted(RESOURCES_DIR.rglob("*Client.py")):
        if path.name.startswith("Async"):
            continue
        clients.append(path)
    return clients


def output_path(sync_path: Path) -> Path:
    return sync_path.with_name(f"Async{sync_path.name}")


def main() -> int:
    check_mode = "--check" in sys.argv
    failures = []

    for sync_path in find_sync_clients():
        source = sync_path.read_text()
        source_rel = str(sync_path.relative_to(REPO_ROOT))
        generated = transform(source, source_rel)
        out = output_path(sync_path)

        if check_mode:
            if not out.exists() or out.read_text() != generated:
                print(f"OUT OF DATE: {out.relative_to(REPO_ROOT)}")
                failures.append(out)
        else:
            out.write_text(generated)
            print(f"Generated: {out.relative_to(REPO_ROOT)}")

    if check_mode:
        if failures:
            print(f"\n{len(failures)} file(s) out of date. Run: python scripts/generate_async_clients.py")
            return 1
        print("All async client files are up to date.")
        return 0

    return 0


if __name__ == "__main__":
    sys.exit(main())
