from paddle_billing.EnumStringify import enum_stringify
from paddle_billing.HasParameters import HasParameters

from paddle_billing.Entities.Shared import CatalogType, Status, TaxCategory

from paddle_billing.Exceptions.SdkExceptions.InvalidArgumentException import InvalidArgumentException

from paddle_billing.Resources.Products.Operations.List.Includes import Includes as ProductIncludes
from paddle_billing.Resources.Shared.Operations                 import Pager


class ListProducts(HasParameters):
    def __init__(
        self,
        pager:          Pager | None          = None,
        includes:       list[ProductIncludes] = None,
        ids:            list[str]             = None,
        types:          list[CatalogType]     = None,
        product_ids:    list[str]             = None,
        statuses:       list[Status]          = None,
        tax_categories: list[TaxCategory]     = None,
    ):
        self.pager          = pager
        self.includes       = includes       if includes       is not None else []
        self.ids            = ids            if ids            is not None else []
        self.types          = types          if types          is not None else []
        self.product_ids    = product_ids    if product_ids    is not None else []
        self.statuses       = statuses       if statuses       is not None else []
        self.tax_categories = tax_categories if tax_categories is not None else []

        # Validation
        for field_name, field_value, field_type in [
            ('ids',            self.ids,            str),
            ('includes',       self.includes,       ProductIncludes),
            ('statuses',       self.statuses,       Status),
            ('tax_categories', self.tax_categories, TaxCategory),
            ('types',          self.types,          CatalogType),
        ]:
            invalid_items = [item for item in field_value if not isinstance(item, field_type)]
            if invalid_items:
                raise InvalidArgumentException(field_name, field_type.__name__, invalid_items)


    def get_parameters(self) -> dict:
        parameters = {}
        if self.pager:
            parameters.update(self.pager.get_parameters())
        if self.ids:
            parameters['id'] = ','.join(self.ids)
        if self.includes:
            parameters['include'] = ','.join(map(enum_stringify, self.includes))
        if self.statuses:
            parameters['status'] = ','.join(map(enum_stringify, self.statuses))
        if self.tax_categories:
            parameters['tax_category'] = ','.join(map(enum_stringify, self.tax_categories))
        if self.types:
            parameters['type'] = ','.join(map(enum_stringify, self.types))

        return parameters
