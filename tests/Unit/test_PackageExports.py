import ast
from pathlib import Path

from pytest import mark

PACKAGE = Path(__file__).parents[2] / "paddle_billing"
INIT_FILES = sorted(PACKAGE.rglob("__init__.py"))
MODULE_FILES = sorted(
    f
    for f in [
        PACKAGE / "Client.py",
        *(PACKAGE / "Entities").glob("*.py"),
        *(PACKAGE / "Notifications/Entities").glob("*.py"),
    ]
    if f.name != "__init__.py"
)


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


def plain_sdk_imports(module_file: Path) -> list[str]:
    tree = ast.parse(module_file.read_text())

    return [
        alias.name
        for node in tree.body
        if isinstance(node, ast.ImportFrom) and (node.module or "").startswith("paddle_billing")
        for alias in node.names
        if alias.asname is None
    ]


def test_module_files_are_found():
    assert PACKAGE / "Client.py" in MODULE_FILES
    assert PACKAGE / "Entities" / "Transaction.py" in MODULE_FILES
    assert PACKAGE / "Notifications" / "Entities" / "Transaction.py" in MODULE_FILES


def test_package_is_marked_as_typed():
    assert (PACKAGE / "py.typed").is_file()


# Type checkers treat a plain `from m import X` in a py.typed package as private, so `from package import X` fails.
@mark.parametrize("init_file", INIT_FILES, ids=lambda f: str(f.relative_to(PACKAGE.parent)))
def test_package_imports_are_explicit_re_exports(init_file):
    assert private_imports(init_file) == []


# Users import resource clients from `paddle_billing.Client`, and enums and nested entities from entity modules.
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
