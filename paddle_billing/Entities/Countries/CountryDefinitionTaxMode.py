from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class CountryDefinitionTaxMode(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Internal: "CountryDefinitionTaxMode" = member("internal")
    External: "CountryDefinitionTaxMode" = member("external")
