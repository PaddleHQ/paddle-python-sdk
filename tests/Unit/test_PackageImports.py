from importlib import import_module
from pathlib import Path

from pytest import mark

PACKAGE = Path(__file__).parents[2] / "paddle_billing"
MODULES = sorted(
    ".".join(path.relative_to(PACKAGE.parent).with_suffix("").parts).removesuffix(".__init__")
    for path in PACKAGE.rglob("*.py")
)


# Catches broken imports in modules that nothing else in the SDK or its tests imports.
@mark.parametrize("module", MODULES)
def test_module_imports(module):
    import_module(module)
