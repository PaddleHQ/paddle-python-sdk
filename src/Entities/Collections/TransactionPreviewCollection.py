from src.Entities.TransactionPreview import TransactionPreview

from src.Entities.Collections.Collection import Collection


class TransactionPreviewCollection(Collection):
    @classmethod
    def from_array(cls, items_data, paginator=None):
        items = [TransactionPreview.from_dict(item) for item in items_data]
        return cls(items, paginator)


    def __next__(self):
        return super().__next__()
