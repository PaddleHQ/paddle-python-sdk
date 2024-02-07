from paddle_billing.EnumStringify import enum_stringify
from paddle_billing.HasParameters import HasParameters

from paddle_billing.Entities.Shared import CollectionMode, TransactionStatus

from paddle_billing.Exceptions.SdkExceptions.InvalidArgumentException import InvalidArgumentException

from paddle_billing.Resources.Shared.Operations                     import DateComparison, Pager
from paddle_billing.Resources.Transactions.Operations.List.Includes import Includes
from paddle_billing.Resources.Transactions.Operations.List.Origin   import Origin


class ListTransactions(HasParameters):
    def __init__(
        self,
        pager:              Pager          | None   = None,
        billed_at:          DateComparison | None   = None,
        collection_mode:    CollectionMode | None   = None,
        created_at:         DateComparison | None   = None,
        updated_at:         DateComparison | None   = None,
        customer_ids:       list[str]               = None,
        ids:                list[str]               = None,
        includes:           list[Includes]          = None,
        invoice_numbers:    list[str]               = None,
        statuses:           list[TransactionStatus] = None,
        subscription_ids:   list[str]               = None,
        origins:            list[Origin]            = None,
    ):
        self.pager            = pager
        self.billed_at        = billed_at
        self.collection_mode  = collection_mode
        self.created_at       = created_at
        self.updated_at       = updated_at
        self.includes         = includes         if includes         is not None else []
        self.ids              = ids              if ids              is not None else []
        self.customer_ids     = customer_ids     if customer_ids     is not None else []
        self.subscription_ids = subscription_ids if subscription_ids is not None else []
        self.invoice_numbers  = invoice_numbers  if invoice_numbers  is not None else []
        self.statuses         = statuses         if statuses         is not None else []
        self.origins          = origins          if origins          is not None else []

        # Validation
        for field_name, field_value, field_type in [
            ('ids',              self.ids,              str),
            ('customer_ids',     self.customer_ids,     str),
            ('subscription_ids', self.subscription_ids, str),
            ('invoice_numbers',  self.invoice_numbers,  str),
            ('includes',         self.includes,         Includes),
            ('statuses',         self.statuses,         TransactionStatus),
            ('origins',          self.origins,          Origin),
        ]:
            invalid_items = [item for item in field_value if not isinstance(item, field_type)]
            if invalid_items:
                raise InvalidArgumentException(field_name, field_type.__name__, invalid_items)


    def get_parameters(self) -> dict:
        parameters = {}
        if self.pager:
            parameters.update(self.pager.get_parameters())

        if self.billed_at is not None:
            parameters[f"billed_at{self.billed_at.comparator}"] = self.billed_at.formatted()
        if self.created_at is not None:
            parameters[f"created_at{self.created_at.comparator}"] = self.created_at.formatted()
        if self.updated_at is not None:
            parameters[f"updated_at{self.updated_at.comparator}"] = self.updated_at.formatted()

        if self.collection_mode:
            parameters['collection_mode'] = self.collection_mode.value
        if self.customer_ids:
            parameters['customer_id'] = ','.join(self.customer_ids)
        if self.ids:
            parameters['id'] = ','.join(self.ids)
        if self.includes:
            parameters['include'] = ','.join(map(enum_stringify, self.includes))
        if self.invoice_numbers:
            parameters['invoice_number'] = ','.join(self.invoice_numbers)
        if self.statuses:
            parameters['status'] = ','.join(map(enum_stringify, self.statuses))
        if self.subscription_ids:
            parameters['subscription_id'] = ','.join(self.subscription_ids)
        if self.origins:
            parameters['origin'] = ','.join(map(enum_stringify, self.origins))

        return parameters
