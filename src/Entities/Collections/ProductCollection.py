from src.Entities.Product import Product

from src.Entities.Collections.Collection import Collection


class ProductCollection(Collection):
    @classmethod
    def from_array(cls, items_data, paginator=None):
        items = [Product.from_dict(item) for item in items_data]
        return cls(items, paginator)


    def __next__(self):
        return super().__next__()
