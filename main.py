from chaining_iterator import I

if __name__ == "__main__":
    # print(list(I([1, 2, 3])))
    # print(I([1, 2, 3]).filter(lambda item: item == 2))
    # print(I([1, 2, 3]).filter(lambda item: item == 2).list())
    # print(I([1, 2, 3]).filter(lambda item: item == 2).each(
    #     lambda item: print(item)))
    # print(I([1, 2, 3]).reduce(lambda value, item: value + item, 0))
    # result = (I([1, 2, 3, 4, 5, 6])
    #     .filter(lambda item: item > 2)
    #     .map(lambda item: item * 3)
    #     .list())
    # print(result)
    result = (I([[1, 2], [3, 4], [5, 6]])
        .flatten()
        .sum())
    print(result)