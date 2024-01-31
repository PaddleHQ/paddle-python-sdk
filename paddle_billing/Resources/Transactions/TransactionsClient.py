from typing import TYPE_CHECKING

from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Transaction                       import Transaction
from paddle_billing.Entities.TransactionData                   import TransactionData
from paddle_billing.Entities.TransactionPreview                import TransactionPreview
from paddle_billing.Entities.Collections.Paginator             import Paginator
from paddle_billing.Entities.Collections.TransactionCollection import TransactionCollection

from paddle_billing.Exceptions.SdkExceptions.InvalidArgumentException import InvalidArgumentException

from paddle_billing.Resources.Transactions.Operations.CreateTransaction  import CreateTransaction
from paddle_billing.Resources.Transactions.Operations.ListTransactions   import ListTransactions
from paddle_billing.Resources.Transactions.Operations.UpdateTransaction  import UpdateTransaction
from paddle_billing.Resources.Transactions.Operations.PreviewTransaction import PreviewTransaction
from paddle_billing.Resources.Transactions.Operations.List.Includes      import Includes


if TYPE_CHECKING:
    from paddle_billing.Client import Client


class TransactionsClient:
    def __init__(self, client: 'Client'):
        self.client   = client
        self.response = None


    def list(self, operation: ListTransactions = None) -> TransactionCollection:
        if operation is None:
            operation = ListTransactions()

        self.response = self.client.get_raw('/transactions', operation.get_parameters())
        parser        = ResponseParser(self.response)

        return TransactionCollection.from_list(
            parser.get_data(),
            Paginator(self.client, parser.get_pagination(), TransactionCollection)
        )


    def get(self, transaction_id: str, includes = None) -> Transaction:
        if includes is None:
            includes = []

        invalid_items = [item for item in includes if not isinstance(item, Includes)]
        if invalid_items:
            raise InvalidArgumentException('includes', Includes.__name__, invalid_items)

        params        = {'include': ','.join(include.value for include in includes)} if includes else {}
        self.response = self.client.get_raw(f"/transactions/{transaction_id}", params)
        parser        = ResponseParser(self.response)

        return Transaction.from_dict(parser.get_data())


    def create(self, operation: CreateTransaction, includes = None) -> Transaction:
        if includes is None:
            includes = []

        invalid_items = [item for item in includes if not isinstance(item, Includes)]
        if invalid_items:
            raise InvalidArgumentException('includes', Includes.__name__, invalid_items)

        params        = {'include': ','.join(include.value for include in includes)} if includes else {}
        self.response = self.client.post_raw('/transactions', operation.get_parameters(), params)
        parser        = ResponseParser(self.response)

        return Transaction.from_dict(parser.get_data())


    def update(self, transaction_id: str, operation: UpdateTransaction) -> Transaction:
        self.response = self.client.patch_raw(f"/transactions/{transaction_id}", operation.get_parameters())
        parser        = ResponseParser(self.response)

        return Transaction.from_dict(parser.get_data())


    def preview(self, operation: PreviewTransaction) -> TransactionPreview:
        self.response = self.client.post_raw('/transactions/preview', operation.get_parameters())
        parser        = ResponseParser(self.response)

        return TransactionPreview.from_dict(parser.get_data())


    def get_invoice_pdf(self, transaction_id: str) -> TransactionData:
        self.response = self.client.get_raw(f"/transactions/{transaction_id}/invoice")
        parser        = ResponseParser(self.response)

        return TransactionData.from_dict(parser.get_data())
