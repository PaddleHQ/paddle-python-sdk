from src.Entities.ProductWithIncludes import ProductWithIncludes

from src.Entities.Collections.Collection import Collection


class ProductWithIncludesCollection(Collection):
    @classmethod
    def from_list(cls, items_data, paginator=None):
        items = [ProductWithIncludes.from_dict(item) for item in items_data]
        return cls(items, paginator)


    def __next__(self):
        return super().__next__()
