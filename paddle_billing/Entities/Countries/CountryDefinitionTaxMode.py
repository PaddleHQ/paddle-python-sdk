from paddle_billing.PaddleStrEnum import (
    PaddleStrEnum as PaddleStrEnum,
    PaddleStrEnumMeta as PaddleStrEnumMeta,
    member as member,
)


class CountryDefinitionTaxMode(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Internal: "CountryDefinitionTaxMode" = member("internal")
    External: "CountryDefinitionTaxMode" = member("external")
