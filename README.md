# Chaining Iterator

**Project status: Early development, not for production**

An iterator to make function chaining possible with some extra features.

## Example

```python
import I from chaining_iterator

result = (I([1, 2, 3, 4, 5, 6])
    .filter(lambda item: item > 2)
    .map(lambda item: item * 3)
    .list())
# [9, 12, 15, 18]

result = (I([[1, 2], [3, 4], [5, 6]])
    .flatten()
    .sum())
# 21
```
