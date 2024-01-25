from paddle_billing_python_sdk.Entities.TransactionWithIncludes import TransactionWithIncludes

from paddle_billing_python_sdk.Entities.Collections.Collection import Collection


class TransactionWithIncludesCollection(Collection):
    @classmethod
    def from_list(cls, items_data, paginator=None):
        items = [TransactionWithIncludes.from_dict(item) for item in items_data]
        return cls(items, paginator)


    def __next__(self):
        return super().__next__()
