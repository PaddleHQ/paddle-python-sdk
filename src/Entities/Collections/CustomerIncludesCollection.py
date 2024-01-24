from src.Entities.CustomerIncludes import CustomerIncludes

from src.Entities.Collections.Collection import Collection


class CustomerIncludesCollection(Collection):
    @classmethod
    def from_array(cls, items_data, paginator=None):
        items = [CustomerIncludes.from_dict(item) for item in items_data]
        return cls(items, paginator)


    def __next__(self):
        return super().__next__()
