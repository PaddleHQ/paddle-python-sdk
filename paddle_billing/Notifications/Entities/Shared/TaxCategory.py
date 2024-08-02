from paddle_billing.PaddleStrEnum import PaddleStrEnum, PaddleStrEnumMeta


class TaxCategory(PaddleStrEnum, metaclass=PaddleStrEnumMeta):
    DigitalGoods                = 'digital-goods'
    Ebooks                      = 'ebooks'
    ImplementationServices      = 'implementation-services'
    ProfessionalServices        = 'professional-services'
    Saas                        = 'saas'
    SoftwareProgrammingServices = 'software-programming-services'
    Standard                    = 'standard'
    TrainingServices            = 'training-services'
    WebsiteHosting              = 'website-hosting'
