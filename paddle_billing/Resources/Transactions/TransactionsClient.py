from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Transaction import Transaction
from paddle_billing.Entities.TransactionData import TransactionData
from paddle_billing.Entities.TransactionPreview import TransactionPreview
from paddle_billing.Entities.Collections import TransactionCollection

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
    from paddle_billing.Client import Client


class TransactionsClient:
    def __init__(self, client: "Client"):
        self.client = client
        self.response = None

    def list(self, operation: ListTransactions | None = None) -> TransactionCollection:
        if operation is None:
            operation = ListTransactions()

        def parse(response):
            self.response = response
            parser = ResponseParser(response)
            return TransactionCollection.from_list(
                parser.get_list(), self.client._make_paginator(parser.get_pagination(), TransactionCollection)
            )
        return self.client._get("/transactions", operation.get_parameters(), parse)

    def get(self, transaction_id: str, includes=None) -> Transaction:
        if includes is None:
            includes = []

        invalid_items = [item for item in includes if not isinstance(item, TransactionIncludes)]
        if invalid_items:
            raise InvalidArgumentException.array_contains_invalid_types(
                "includes", TransactionIncludes.__name__, invalid_items
            )

        params = {"include": ",".join(include.value for include in includes)} if includes else {}

        def parse(response):
            self.response = response
            return Transaction.from_dict(ResponseParser(response).get_dict())
        return self.client._get(f"/transactions/{transaction_id}", params, parse)

    def create(self, operation: CreateTransaction, includes=None) -> Transaction:
        if includes is None:
            includes = []

        invalid_items = [item for item in includes if not isinstance(item, TransactionIncludes)]
        if invalid_items:
            raise InvalidArgumentException.array_contains_invalid_types(
                "includes", TransactionIncludes.__name__, invalid_items
            )

        params = {"include": ",".join(include.value for include in includes)} if includes else {}

        def parse(response):
            self.response = response
            return Transaction.from_dict(ResponseParser(response).get_dict())
        return self.client._post("/transactions", operation, parse, params)

    def update(self, transaction_id: str, operation: UpdateTransaction) -> Transaction:
        def parse(response):
            self.response = response
            return Transaction.from_dict(ResponseParser(response).get_dict())
        return self.client._patch(f"/transactions/{transaction_id}", operation, parse)

    def preview(
        self,
        operation: (
            PreviewTransaction | PreviewTransactionByAddress | PreviewTransactionByCustomer | PreviewTransactionByIP
        ),
    ) -> TransactionPreview:
        def parse(response):
            self.response = response
            return TransactionPreview.from_dict(ResponseParser(response).get_dict())
        return self.client._post("/transactions/preview", operation, parse)

    def get_invoice_pdf(self, transaction_id: str, operation: GetTransactionInvoice | None = None) -> TransactionData:
        def parse(response):
            self.response = response
            return TransactionData.from_dict(ResponseParser(response).get_dict())
        return self.client._get(f"/transactions/{transaction_id}/invoice", operation, parse)

    def revise(self, transaction_id: str, operation: ReviseTransaction) -> Transaction:
        def parse(response):
            self.response = response
            return Transaction.from_dict(ResponseParser(response).get_dict())
        return self.client._post(f"/transactions/{transaction_id}/revise", operation, parse)
