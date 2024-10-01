from dataclasses import asdict, dataclass, is_dataclass

from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


def test_paddle_str_enum_works_as_expected():
    class TestCountryCodesEnum(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
        CA: "TestCountryCodesEnum" = "canada"
        US: "TestCountryCodesEnum" = "usa"

    assert isinstance(TestCountryCodesEnum.CA, TestCountryCodesEnum)
    assert isinstance(TestCountryCodesEnum.US, TestCountryCodesEnum)
    assert isinstance(TestCountryCodesEnum("canada"), TestCountryCodesEnum)
    assert isinstance(TestCountryCodesEnum("usa"), TestCountryCodesEnum)
    assert TestCountryCodesEnum.CA == "canada"
    assert TestCountryCodesEnum.US == "usa"
    assert TestCountryCodesEnum("canada") == "canada"
    assert TestCountryCodesEnum("usa") == "usa"
    assert TestCountryCodesEnum.CA.name == "CA"
    assert TestCountryCodesEnum("canada").name == "CA"


def test_dataclass_asdict_returns_expected_paddle_str_enum_value():
    class TestCountryCodesEnum(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
        CA: "TestCountryCodesEnum" = "canada"
        US: "TestCountryCodesEnum" = "usa"

    @dataclass
    class TestDataclass:
        country_code: TestCountryCodesEnum = None

        def get_parameters(self) -> dict:
            return asdict(self)

    test_dataclass = TestDataclass(TestCountryCodesEnum.CA)
    assert is_dataclass(test_dataclass)
    assert isinstance(test_dataclass.get_parameters(), dict)
    assert test_dataclass.get_parameters().get("country_code", None) is not None
    assert type(test_dataclass.get_parameters().get("country_code", None)) == TestCountryCodesEnum
    assert test_dataclass.get_parameters().get("country_code", None) == "canada"

    # Test for non-existent enum name
    test_dataclass = TestDataclass(TestCountryCodesEnum.FAKE)
    assert is_dataclass(test_dataclass)
    assert isinstance(test_dataclass.get_parameters(), dict)
    assert test_dataclass.get_parameters().get("country_code", None) is not None
    assert isinstance(test_dataclass.get_parameters().get("country_code", None), TestCountryCodesEnum)
    assert test_dataclass.get_parameters().get("country_code", TestCountryCodesEnum.CA).is_known() is False


def test_paddle_str_enum_gracefully_handles_missing_values():
    class TestCountryCodesEnum(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
        CA: "TestCountryCodesEnum" = "canada"
        US: "TestCountryCodesEnum" = "usa"

    assert isinstance(TestCountryCodesEnum.FR, TestCountryCodesEnum)
    assert isinstance(TestCountryCodesEnum("france"), TestCountryCodesEnum)

    # Via constructor
    assert TestCountryCodesEnum("france") == "france"
    assert TestCountryCodesEnum("france").value == "france"
    assert TestCountryCodesEnum("france").name == "Undefined"
    assert not TestCountryCodesEnum("france").is_known()

    # Via missing attr
    assert TestCountryCodesEnum.France == "france"
    assert TestCountryCodesEnum.France.value == "france"
    assert TestCountryCodesEnum.France.name == "Undefined"
    assert not TestCountryCodesEnum.France.is_known()
