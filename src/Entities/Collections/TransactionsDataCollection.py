from src.Entities.TransactionData import TransactionData

from src.Entities.Collections.Collection import Collection


class TransactionsDataCollection(Collection):
    @classmethod
    def from_array(cls, items_data, paginator=None):
        items = [TransactionData.from_dict(item) for item in items_data]
        return cls(items, paginator)


    def __next__(self):
        return super().__next__()
