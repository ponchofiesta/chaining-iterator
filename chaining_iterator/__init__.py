import functools
import itertools
from typing import Any, Callable, Iterable


class ChainingIterator:
    def __init__(self, iterable: Iterable) -> None:
        self.iterable = iter(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iterable)

    def filter(self, predicate: Callable[[Any], Any]) -> 'ChainingIterator':
        return ChainingIterator(filter(predicate, self.iterable))

    def map(self, f: Callable) -> 'ChainingIterator':
        return ChainingIterator(map(f, self.iterable))

    def map_while(self, predicate: Callable) -> Iterable:
        ...

    def zip(self, other: Iterable) -> Iterable:
        return ChainingIterator(zip(self.iterable, other))

    def unzip(self) -> tuple[Iterable, Iterable]:
        return ChainingIterator(zip(*self.iterable))

    def flatten(self):
        return ChainingIterator([item for iterable in self.iterable for item in iterable])

    def __skip(self, n: int):
        pos = 0
        for item in self.iterable:
            if pos >= n:
                yield item
            pos += 1

    def skip(self, n: int):
        return ChainingIterator(self.__skip(n))

    def skip_while(self, predicate: Callable) -> Iterable:
        return ChainingIterator(itertools.dropwhile(predicate, self.iterable))

    def __take(self, n: int):
        pos = 0
        for item in self.iterable:
            if pos == n:
                break
            yield item
            pos += 1

    def take(self, n: int) -> Iterable:
        return ChainingIterator(self.__take(n))

    def take_while(self, predicate: Callable) -> Iterable:
        return ChainingIterator(itertools.takewhile(predicate, self.iterable))

    def repeat(self, n: int) -> Iterable:
        ...

    def chain(self, *others: Iterable) -> Iterable:
        return ChainingIterator(itertools.chain(self.iterable, *others))

    def each(self, f: Callable[[Any], None]) -> None:
        for item in self.iterable:
            f(item)

    def reduce(self, f: Callable, initial: Any = None) -> Any:
        return functools.reduce(f, self.iterable, initial)

    def list(self) -> list:
        return list(self.iterable)

    def sort(self) -> list:
        ...

    def eq(self, other: Iterable) -> bool:
        ...

    def ne(self, other: Iterable) -> bool:
        ...

    def lt(self, other: Iterable) -> bool:
        ...

    def le(self, other: Iterable) -> bool:
        ...

    def gt(self, other: Iterable) -> bool:
        ...

    def ge(self, other: Iterable) -> bool:
        ...

    def all(self, f: Callable) -> bool:
        for item in self.iterable:
            if not f(item):
                return False
        return True

    def any(self, f: Callable) -> bool:
        for item in self.iterable:
            if f(item):
                return True
        return False

    def count(self) -> int:
        return sum(1 for _ in self.iterable)

    def len(self) -> int:
        return self.count()

    def min(self) -> Any:
        return min(self.iterable)

    def max(self) -> Any:
        return max(self.iterable)

    def sum(self) -> Any:
        return sum(self.iterable)

    def product(self) -> Any:
        return functools.reduce(lambda item, value: item * value, self.iterable, 1)

    def permutations(self, k: int) -> Any:
        return ChainingIterator(itertools.permutations(self.iterable, k))

    def position(self, predicate: Callable) -> int | None:
        for index, item in enumerate(self.iterable):
            if predicate(item):
                return index
        return None

    def find(self, predicate: Callable[[Any], Any]) -> Any:
        return next(filter(predicate, self.iterable), None)

    def last(self) -> Any:
        return functools.reduce(lambda _, value: value, self.iterable, None)

    def __join(self, sepearator: Any) -> Any:
        ...

    def join(self, seperator: Any) -> Any:
        ...

    def concat(self) -> Any:
        ...

    def split(self, predicate: Callable) -> Iterable:
        return ChainingIterator()

    def reverse(self):
        return ChainingIterator(reversed(list(self.iterable)))

    def __fill(self, value):
        for _ in self.iterable:
            yield value

    def fill(self, value: Any) -> Iterable:
        return ChainingIterator(self.__fill(value))


I = ChainingIterator
