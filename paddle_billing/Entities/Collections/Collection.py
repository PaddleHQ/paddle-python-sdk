from abc             import ABC, abstractmethod
from collections.abc import Iterator

from paddle_billing.Entities.Collections.Paginator import Paginator


class Collection(ABC, Iterator):
    def __init__(self, items, paginator: Paginator | None = None):
        self.items     = items
        self.paginator = paginator
        self._pointer  = 0


    @abstractmethod
    def from_list(self, data, paginator: Paginator | None = None):
        pass


    def __iter__(self):
        self._pointer = 0

        return self


    def __next__(self):
        if self._pointer < len(self.items):
            result         = self.items[self._pointer]
            self._pointer += 1

            return result

        if self.paginator and self.paginator.has_more:
            new_collection = self.paginator.next_page()
            self.items.extend(new_collection.items)  # Append new items
            self.paginator = new_collection.paginator

            return self.__next__()  # Continue iteration with new items

        raise StopIteration


    def current(self):
        return self.items[self._pointer]


    def key(self):
        return getattr(self.items[self._pointer], 'id', self._pointer)
