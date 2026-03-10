import inspect

from abc import ABC, abstractmethod
from collections.abc import AsyncIterator, Iterator
from typing import TypeVar, Generic

from paddle_billing.Entities.Collections.Paginator import Paginator

T = TypeVar("T")


class Collection(ABC, Generic[T], Iterator[T], AsyncIterator[T]):
    def __init__(self, items, paginator: Paginator | None = None):
        self.items = items
        self.paginator = paginator
        self._pointer = 0

    @abstractmethod
    def from_list(self, data, paginator: Paginator | None = None):
        pass

    def __iter__(self) -> Iterator[T]:
        self._pointer = 0

        return self

    def __next__(self) -> T:
        if self._pointer < len(self.items):
            result = self.items[self._pointer]
            self._pointer += 1

            return result

        if self.paginator and self.paginator.has_more:
            new_collection = self.paginator.next_page()
            self.items.extend(new_collection.items)  # Append new items
            self.paginator = new_collection.paginator

            return self.__next__()  # Continue iteration with new items

        raise StopIteration

    def __aiter__(self) -> AsyncIterator[T]:
        self._pointer = 0

        return self

    async def __anext__(self) -> T:
        if self._pointer < len(self.items):
            result = self.items[self._pointer]
            self._pointer += 1

            return result

        if self.paginator and self.paginator.has_more:
            next_page = self.paginator.next_page()
            new_collection = await next_page if inspect.isawaitable(next_page) else next_page
            self.items.extend(new_collection.items)  # Append new items
            self.paginator = new_collection.paginator

            return await self.__anext__()  # Continue iteration with new items

        raise StopAsyncIteration

    def current(self) -> T:
        return self.items[self._pointer]

    def key(self) -> str:
        return getattr(self.items[self._pointer], "id", self._pointer)
