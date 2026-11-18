import ast
from pathlib import Path

from pytest import mark

PACKAGE = Path(__file__).parents[2] / "paddle_billing"
INIT_FILES = sorted(PACKAGE.rglob("__init__.py"))


def private_imports(init_file: Path) -> list[str]:
    tree = ast.parse(init_file.read_text())
    exported = set()
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(getattr(t, "id", None) == "__all__" for t in node.targets):
            exported = set(ast.literal_eval(node.value))

    return [
        alias.asname or alias.name
        for node in tree.body
        if isinstance(node, ast.ImportFrom)
        for alias in node.names
        if alias.asname != alias.name and (alias.asname or alias.name) not in exported
    ]


def test_package_is_marked_as_typed():
    assert (PACKAGE / "py.typed").is_file()


# Type checkers treat a plain `from m import X` in a py.typed package as private, so `from package import X` fails.
@mark.parametrize("init_file", INIT_FILES, ids=lambda f: str(f.relative_to(PACKAGE.parent)))
def test_package_imports_are_explicit_re_exports(init_file):
    assert private_imports(init_file) == []
