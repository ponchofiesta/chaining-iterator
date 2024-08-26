import functools
import itertools
from typing import Callable, Generic, Iterable, Iterator, List, Optional, TypeVar

T = TypeVar('T')
U = TypeVar('U')
V = TypeVar('V')

class ChainingIterator(Generic[T]):
    def __init__(self, iterable: Iterable[T]) -> None:
        self.iterable = iter(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iterable)

    def filter(self, predicate: Callable[[T], T]) -> 'ChainingIterator[T]':
        return ChainingIterator(filter(predicate, self.iterable))

    def map(self, f: Callable[[T], U]) -> 'ChainingIterator[U]':
        return ChainingIterator(map(f, self.iterable))

    def map_while(self, predicate: Callable[[T], U]) -> 'ChainingIterator[U]':
        ...

    def zip(self, other: Iterable[T]) -> 'ChainingIterator[Iterator[T]]':
        return ChainingIterator(zip(self.iterable, other))

    def unzip(self) -> tuple[Iterator[U], Iterator[U]]:
        return ChainingIterator(zip(*self.iterable))

    def flatten(self) -> 'ChainingIterator':
        return ChainingIterator([item for iterable in self.iterable for item in iterable])

    def __skip(self, n: int) -> Iterator[T]:
        pos = 0
        for item in self.iterable:
            if pos >= n:
                yield item
            pos += 1

    def skip(self, n: int) -> 'ChainingIterator[T]':
        return ChainingIterator(self.__skip(n))

    def skip_while(self, predicate: Callable[[T], bool]) -> 'ChainingIterator[T]':
        return ChainingIterator(itertools.dropwhile(predicate, self.iterable))

    def __take(self, n: int) -> Iterator[T]:
        pos = 0
        for item in self.iterable:
            if pos == n:
                break
            yield item
            pos += 1

    def take(self, n: int) -> 'ChainingIterator[T]':
        return ChainingIterator(self.__take(n))

    def take_while(self, predicate: Callable[[T], bool]) -> 'ChainingIterator[T]':
        return ChainingIterator(itertools.takewhile(predicate, self.iterable))

    def repeat(self, n: int) -> 'ChainingIterator[T]':
        ...

    def chain(self, *others: Iterable[T]) -> 'ChainingIterator[T]':
        return ChainingIterator(itertools.chain(self.iterable, *others))

    def each(self, f: Callable[[T], None]) -> None:
        for item in self.iterable:
            f(item)

    def reduce(self, f: Callable[[T, T], T], initial: Optional[T] = None) -> T:
        if initial is None:
            return functools.reduce(f, self.iterable)
        else:
            return functools.reduce(f, self.iterable, initial)

    def list(self) -> list[T]:
        return list(self.iterable)

    def sort(self) -> List[T]:
        return sorted(self.iterable)

    def eq(self, other: Iterable[T]) -> bool:
        ...

    def ne(self, other: Iterable[T]) -> bool:
        ...

    def lt(self, other: Iterable[T]) -> bool:
        ...

    def le(self, other: Iterable[T]) -> bool:
        ...

    def gt(self, other: Iterable[T]) -> bool:
        ...

    def ge(self, other: Iterable[T]) -> bool:
        ...

    def all(self, f: Callable[[T], bool]) -> bool:
        for item in self.iterable:
            if not f(item):
                return False
        return True

    def any(self, f: Callable[[T], bool]) -> bool:
        for item in self.iterable:
            if f(item):
                return True
        return False

    def count(self) -> int:
        return sum(1 for _ in self.iterable)

    def len(self) -> int:
        return self.count()

    def min(self) -> T:
        return min(self.iterable)

    def max(self) -> T:
        return max(self.iterable)

    def sum(self) -> T:
        return sum(self.iterable)

    def product(self) -> T:
        return functools.reduce(lambda item, value: item * value, self.iterable, 1)

    def permutations(self, k: int) -> 'ChainingIterator[tuple[T, ...]]':
        return ChainingIterator(itertools.permutations(self.iterable, k))

    def position(self, predicate: Callable[[T], int | None]) -> int | None:
        for index, item in enumerate(self.iterable):
            if predicate(item):
                return index
        return None

    def find(self, predicate: Callable[[T], T]) -> T | None:
        return next(filter(predicate, self.iterable), None)
    
    def first(self) -> T | None:
        return next(self.iterable, None)

    def last(self) -> T | None:
        return functools.reduce(lambda _, value: value, self.iterable, None)

    def __join(self, sepearator: T | Iterable[T]) -> 'ChainingIterator[T]':
        ...

    def join(self, seperator: T | Iterable[T]) -> 'ChainingIterator[T]':
        ...

    def concat(self) -> 'ChainingIterator[T]':
        ...

    def split(self, predicate: Callable[[T], bool]) -> 'ChainingIterator[list[T]]':
        ...

    def reverse(self) -> 'ChainingIterator[T]':
        return ChainingIterator(reversed(list(self.iterable)))

    def __fill(self, value: U) -> Iterator[U]:
        for _ in self.iterable:
            yield value

    def fill(self, value: U) -> 'ChainingIterator[U]':
        return ChainingIterator(self.__fill(value))

    def batched(self, n: int) -> 'ChainingIterator[tuple[T, ...]]':
        ...
    
    def chunks(self, n: int) -> 'ChainingIterator[tuple[T, ...]]':
        return self.batched(n)
    
    def chunks_exact(self, n: int) -> 'ChainingIterator[tuple[T, ...]]':
        ...
    
    def chunks_by(self, predicate: Callable) -> 'ChainingIterator[tuple[T, ...]]':
        ...
    
    def windows(self, n: int) -> 'ChainingIterator[tuple[T, ...]]':
        ...

    def starts_with(self, prefix: Iterable[T]) -> bool:
        ...
        
    def ends_with(self, suffix: Iterable[T]) -> bool:
        ...
        
    


I = ChainingIterator
