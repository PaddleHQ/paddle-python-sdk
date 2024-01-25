from abc import ABC, abstractmethod
from collections.abc import Iterator


class Collection(ABC, Iterator):
    def __init__(self, items, paginator=None):
        self._items = items
        self._paginator = paginator
        self._pointer = 0


    @abstractmethod
    def from_list(cls, data, paginator=None):
        pass


    def __iter__(self):
        self._pointer = 0
        return self


    def __next__(self):
        if self._pointer < len(self._items):
            result         = self._items[self._pointer]
            self._pointer += 1
            return result

        if self._paginator and self._paginator.has_more():
            collection      = self._paginator.next_page()
            self._items     = collection.items
            self._paginator = collection.paginator
            return self.__next__()

        raise StopIteration


    def current(self):
        return self._items[self._pointer]


    def key(self):
        item = self._items[self._pointer]
        return getattr(item, 'id', self._pointer)
