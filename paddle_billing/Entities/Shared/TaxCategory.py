from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta, member


class TaxCategory(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    DigitalGoods: "TaxCategory" = member("digital-goods")
    Ebooks: "TaxCategory" = member("ebooks")
    ImplementationServices: "TaxCategory" = member("implementation-services")
    ProfessionalServices: "TaxCategory" = member("professional-services")
    Saas: "TaxCategory" = member("saas")
    SoftwareProgrammingServices: "TaxCategory" = member("software-programming-services")
    Standard: "TaxCategory" = member("standard")
    TrainingServices: "TaxCategory" = member("training-services")
    WebsiteHosting: "TaxCategory" = member("website-hosting")
