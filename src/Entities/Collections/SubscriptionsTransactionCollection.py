from src.Entities.SubscriptionTransaction import SubscriptionTransaction

from src.Entities.Collections.Collection import Collection


class SubscriptionsTransactionCollection(Collection):
    @classmethod
    def from_array(cls, items_data, paginator=None):
        items = [SubscriptionTransaction.from_dict(item) for item in items_data]
        return cls(items, paginator)


    def __next__(self):
        return super().__next__()
