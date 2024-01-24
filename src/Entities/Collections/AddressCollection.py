from src.Entities.Address import Address

from src.Entities.Collections.Collection import Collection


class AddressCollection(Collection):
    @classmethod
    def from_array(cls, items_data, paginator=None):
        items = [Address.from_dict(item) for item in items_data]
        return cls(items, paginator)


    def __next__(self):
        return super().__next__()  # Calls __next__ from Collection and ensures it returns EventType
