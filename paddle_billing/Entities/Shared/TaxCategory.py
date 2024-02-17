from paddle_billing.PaddleStrEnum import PaddleStrEnum


class TaxCategory(PaddleStrEnum):
    DigitalGoods                = 'digital-goods'
    Ebooks                      = 'ebooks'
    ImplementationServices      = 'implementation-services'
    ProfessionalServices        = 'professional-services'
    Saas                        = 'saas'
    SoftwareProgrammingServices = 'software-programming-services'
    Standard                    = 'standard'
    TrainingServices            = 'training-services'
    WebsiteHosting              = 'website-hosting'
