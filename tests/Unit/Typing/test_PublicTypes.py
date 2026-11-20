from pathlib import Path

from mypy import api
from pytest import fixture, mark

USAGE = Path(__file__).parent / "usage"


@fixture(autouse=True)
def isolated_mypy(monkeypatch, tmp_path):
    # Resolve paddle_billing from this checkout and cache outside it, whatever directory pytest runs from.
    monkeypatch.setenv("MYPYPATH", str(Path(__file__).parents[3]))
    monkeypatch.setenv("MYPY_CACHE_DIR", str(tmp_path))


def type_check(file: Path) -> list[str]:
    # silent: only report errors in the usage file, the way a user's type checker sees the SDK.
    stdout, _, _ = api.run(["--strict", "--follow-imports=silent", "--no-incremental", str(file)])
    return [line for line in stdout.splitlines() if ": error:" in line]


@mark.parametrize("usage", ["client_usage.py", "webhooks.py"])
def test_documented_usage_type_checks(usage):
    assert type_check(USAGE / usage) == []


def test_type_checker_rejects_invalid_usage():
    errors = type_check(USAGE / "invalid_usage.py")

    assert len(errors) == 2, errors
    assert 'Argument 1 to "Client" has incompatible type "int"' in errors[0]
    assert 'Argument 1 to "verify" of "Verifier" has incompatible type "NoBodyRequest"' in errors[1]
