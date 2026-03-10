from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Transaction import Transaction
from paddle_billing.Entities.TransactionData import TransactionData
from paddle_billing.Entities.TransactionPreview import TransactionPreview
from paddle_billing.Entities.Collections import AsyncPaginator, TransactionCollection

from paddle_billing.Exceptions.SdkExceptions.InvalidArgumentException import InvalidArgumentException

from paddle_billing.Resources.Transactions.Operations import (
    CreateTransaction,
    ListTransactions,
    UpdateTransaction,
    PreviewTransaction,
    PreviewTransactionByAddress,
    PreviewTransactionByCustomer,
    PreviewTransactionByIP,
    TransactionIncludes,
    GetTransactionInvoice,
    ReviseTransaction,
)

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.AsyncClient import AsyncClient


class AsyncTransactionsClient:
    def __init__(self, client: "AsyncClient"):
        self.client = client
        self.response = None

    async def list(self, operation: ListTransactions | None = None) -> TransactionCollection:
        if operation is None:
            operation = ListTransactions()

        self.response = await self.client.get_raw("/transactions", operation.get_parameters())
        parser = ResponseParser(self.response)

        return TransactionCollection.from_list(
            parser.get_list(), AsyncPaginator(self.client, parser.get_pagination(), TransactionCollection)
        )

    async def get(self, transaction_id: str, includes=None) -> Transaction:
        if includes is None:
            includes = []

        invalid_items = [item for item in includes if not isinstance(item, TransactionIncludes)]
        if invalid_items:
            raise InvalidArgumentException.array_contains_invalid_types(
                "includes", TransactionIncludes.__name__, invalid_items
            )

        params = {"include": ",".join(include.value for include in includes)} if includes else {}
        self.response = await self.client.get_raw(f"/transactions/{transaction_id}", params)
        parser = ResponseParser(self.response)

        return Transaction.from_dict(parser.get_dict())

    async def create(self, operation: CreateTransaction, includes=None) -> Transaction:
        if includes is None:
            includes = []

        invalid_items = [item for item in includes if not isinstance(item, TransactionIncludes)]
        if invalid_items:
            raise InvalidArgumentException.array_contains_invalid_types(
                "includes", TransactionIncludes.__name__, invalid_items
            )

        params = {"include": ",".join(include.value for include in includes)} if includes else {}
        self.response = await self.client.post_raw("/transactions", operation, params)
        parser = ResponseParser(self.response)

        return Transaction.from_dict(parser.get_dict())

    async def update(self, transaction_id: str, operation: UpdateTransaction) -> Transaction:
        self.response = await self.client.patch_raw(f"/transactions/{transaction_id}", operation)
        parser = ResponseParser(self.response)

        return Transaction.from_dict(parser.get_dict())

    async def preview(
        self,
        operation: (
            PreviewTransaction | PreviewTransactionByAddress | PreviewTransactionByCustomer | PreviewTransactionByIP
        ),
    ) -> TransactionPreview:
        self.response = await self.client.post_raw("/transactions/preview", operation)
        parser = ResponseParser(self.response)

        return TransactionPreview.from_dict(parser.get_dict())

    async def get_invoice_pdf(
        self, transaction_id: str, operation: GetTransactionInvoice | None = None
    ) -> TransactionData:
        self.response = await self.client.get_raw(f"/transactions/{transaction_id}/invoice", operation)
        parser = ResponseParser(self.response)

        return TransactionData.from_dict(parser.get_dict())

    async def revise(self, transaction_id: str, operation: ReviseTransaction) -> Transaction:
        self.response = await self.client.post_raw(f"/transactions/{transaction_id}/revise", operation)
        parser = ResponseParser(self.response)

        return Transaction.from_dict(parser.get_dict())
