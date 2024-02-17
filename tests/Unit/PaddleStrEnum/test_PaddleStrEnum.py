from dataclasses import asdict, dataclass, is_dataclass

from paddle_billing.PaddleStrEnum import PaddleStrEnum
from paddle_billing.Undefined     import Undefined



def test_paddle_str_enum_works_as_expected():
    class TestCountryCodesEnum(PaddleStrEnum):
        CA = 'canada'
        US = 'usa'


    assert isinstance(TestCountryCodesEnum.CA, PaddleStrEnum)
    assert isinstance(TestCountryCodesEnum.US, PaddleStrEnum)
    assert TestCountryCodesEnum.CA == 'canada'
    assert TestCountryCodesEnum.US == 'usa'
    assert TestCountryCodesEnum('canada') == 'canada'
    assert TestCountryCodesEnum('usa')    == 'usa'

    # Test for non-existent enum name
    assert isinstance(TestCountryCodesEnum.FAKE, Undefined)



def test_dataclass_asdict_returns_expected_paddle_str_enum_value():
    class TestCountryCodesEnum(PaddleStrEnum):
        CA = 'canada'
        US = 'usa'


    @dataclass
    class TestDataclass:
        country_code: TestCountryCodesEnum | Undefined = Undefined()

        def get_parameters(self) -> dict:
            return asdict(self)


    test_dataclass = TestDataclass(TestCountryCodesEnum.CA)
    assert is_dataclass(test_dataclass)
    assert isinstance(test_dataclass.get_parameters(), dict)
    assert test_dataclass.get_parameters().get('country_code', None)       is not None
    assert type(test_dataclass.get_parameters().get('country_code', None)) == TestCountryCodesEnum
    assert test_dataclass.get_parameters().get('country_code', None)       == 'canada'

    # Test for non-existent enum name
    test_dataclass = TestDataclass(TestCountryCodesEnum.FAKE)
    assert is_dataclass(test_dataclass)
    assert isinstance(test_dataclass.get_parameters(), dict)
    assert test_dataclass.get_parameters().get('country_code', None)       is not None
    assert type(test_dataclass.get_parameters().get('country_code', None)) == Undefined
