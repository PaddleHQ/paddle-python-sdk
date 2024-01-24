from src.Entities.PriceWithIncludes import PriceWithIncludes

from src.Entities.Collections.Collection import Collection


class PriceWithIncludesCollection(Collection):
    @classmethod
    def from_array(cls, items_data, paginator=None):
        items = [PriceWithIncludes.from_dict(item) for item in items_data]
        return cls(items, paginator)


    def __next__(self):
        return super().__next__()
