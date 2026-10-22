from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class CountryDefinitionTaxMode(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    Internal: "CountryDefinitionTaxMode" = "internal"
    External: "CountryDefinitionTaxMode" = "external"
