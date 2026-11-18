from pathlib import Path

from mypy import api
from pytest import mark

USAGE = Path(__file__).parent / "usage"


def type_check(file: Path) -> list[str]:
    # silent: only report errors in the usage file, the way a user's type checker sees the SDK.
    stdout, _, _ = api.run(["--strict", "--follow-imports=silent", "--no-incremental", str(file)])
    return [line for line in stdout.splitlines() if ": error:" in line]


@mark.parametrize("usage", ["readme.py", "webhooks.py"])
def test_documented_usage_type_checks(usage):
    assert type_check(USAGE / usage) == []


def test_type_checker_rejects_invalid_usage():
    errors = type_check(USAGE / "rejected.py")

    assert any('Argument 1 to "Client" has incompatible type "int"' in error for error in errors)
    assert any('Argument 1 to "verify" of "Verifier"' in error for error in errors)
    assert len(errors) == 2, errors
