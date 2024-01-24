from src.Entities.CreditBalance import CreditBalance

from src.Entities.Collections.Collection import Collection


class CreditBalanceCollection(Collection):
    @classmethod
    def from_array(cls, items_data, paginator=None):
        items = [CreditBalance.from_dict(item) for item in items_data]
        return cls(items, paginator)


    def __next__(self):
        return super().__next__()
