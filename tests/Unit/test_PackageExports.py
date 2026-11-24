import ast
from pathlib import Path

from pytest import mark

PACKAGE = Path(__file__).parents[2] / "paddle_billing"
INIT_FILES = sorted(PACKAGE.rglob("__init__.py"))
MODULE_FILES = sorted(f for f in PACKAGE.rglob("*.py") if f.name != "__init__.py")


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


def module_level_statements(body: list[ast.stmt]) -> list[ast.stmt]:
    # Imports under `if TYPE_CHECKING:` aren't importable at runtime, so they're skipped.
    statements = []
    for node in body:
        statements.append(node)
        if isinstance(node, ast.If) and "TYPE_CHECKING" not in ast.unparse(node.test):
            statements += module_level_statements(node.body + node.orelse)
        elif isinstance(node, ast.Try):
            handler_bodies = [statement for handler in node.handlers for statement in handler.body]
            statements += module_level_statements(node.body + handler_bodies + node.orelse + node.finalbody)
    return statements


def plain_sdk_imports(module_file: Path) -> list[str]:
    tree = ast.parse(module_file.read_text())

    return [
        alias.name
        for node in module_level_statements(tree.body)
        if isinstance(node, ast.ImportFrom) and (node.level > 0 or (node.module or "").startswith("paddle_billing"))
        for alias in node.names
        if alias.asname is None or (alias.asname != alias.name and not alias.asname.startswith("_"))
    ]


def test_module_files_are_found():
    assert PACKAGE / "Client.py" in MODULE_FILES
    assert PACKAGE / "Entities" / "Subscriptions" / "SubscriptionItem.py" in MODULE_FILES
    assert PACKAGE / "Resources" / "Prices" / "Operations" / "ListPrices.py" in MODULE_FILES


def test_package_is_marked_as_typed():
    assert (PACKAGE / "py.typed").is_file()


# Type checkers treat a plain `from m import X` in a py.typed package as private, so `from package import X` fails.
@mark.parametrize("init_file", INIT_FILES, ids=lambda f: str(f.relative_to(PACKAGE.parent)))
def test_package_imports_are_explicit_re_exports(init_file):
    assert private_imports(init_file) == []


# Any name a module imports could be imported from it before py.typed, so every module re-exports its SDK imports.
# A renamed import is never public, so its name must start with `_` (assign it to a public name if users need it).
@mark.parametrize("module_file", MODULE_FILES, ids=lambda f: str(f.relative_to(PACKAGE.parent)))
def test_module_imports_are_explicit_re_exports(module_file):
    assert plain_sdk_imports(module_file) == []


# The names `import *` gave before these packages defined `__all__`, including subpackage modules.
STAR_IMPORTS = {
    "Adjustments": ["Create", "CreateAdjustment", "CreateAdjustmentItem", "GetCreditNote", "ListAdjustments"],
    "Prices": ["CreatePrice", "List", "ListPrices", "PriceIncludes", "UpdatePrice"],
    "Products": ["CreateProduct", "List", "ListProducts", "ProductIncludes", "UpdateProduct"],
    "Subscriptions": [
        "CancelSubscription",
        "Charge",
        "CreateOneTimeCharge",
        "Get",
        "ListSubscriptionHistory",
        "ListSubscriptions",
        "PauseSubscription",
        "PreviewOneTimeCharge",
        "PreviewUpdateSubscription",
        "Price",
        "ResumeSubscription",
        "SubscriptionDiscount",
        "SubscriptionIncludes",
        "Update",
        "UpdateSubscription",
    ],
    "Transactions": [
        "Create",
        "CreateTransaction",
        "Discount",
        "GetTransactionInvoice",
        "List",
        "ListTransactions",
        "Preview",
        "PreviewTransaction",
        "PreviewTransactionByAddress",
        "PreviewTransactionByCustomer",
        "PreviewTransactionByIP",
        "Price",
        "Revise",
        "ReviseTransaction",
        "TransactionIncludes",
        "TransactionOrigin",
        "Update",
        "UpdateTransaction",
    ],
}


@mark.parametrize("resource, expected", STAR_IMPORTS.items(), ids=list(STAR_IMPORTS))
def test_star_import_exports_the_same_names(resource, expected):
    namespace: dict = {}
    exec(f"from paddle_billing.Resources.{resource}.Operations import *", namespace)

    assert sorted(name for name in namespace if not name.startswith("_")) == expected
