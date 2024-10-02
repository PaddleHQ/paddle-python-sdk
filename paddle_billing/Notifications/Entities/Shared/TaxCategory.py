from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class TaxCategory(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    DigitalGoods: "TaxCategory" = "digital-goods"
    Ebooks: "TaxCategory" = "ebooks"
    ImplementationServices: "TaxCategory" = "implementation-services"
    ProfessionalServices: "TaxCategory" = "professional-services"
    Saas: "TaxCategory" = "saas"
    SoftwareProgrammingServices: "TaxCategory" = "software-programming-services"
    Standard: "TaxCategory" = "standard"
    TrainingServices: "TaxCategory" = "training-services"
    WebsiteHosting: "TaxCategory" = "website-hosting"
