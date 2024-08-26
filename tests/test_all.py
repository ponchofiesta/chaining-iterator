from pytest_check import check
from chaining_iterator import I


def test_init():
    actual = list(I([1, 2, 3]))
    check.equal(actual, [1, 2, 3])


def test_filter():
    actual = I([1, 2, 3]).filter(lambda item: item == 2).list()
    check.equal(actual, [2])


def test_list():
    actual = I([1, 2, 3]).list()
    check.equal(actual, [1, 2, 3])


def test_min():
    actual = I([1, 2, 3]).min()
    check.equal(actual, 1)


def test_max():
    actual = I([1, 2, 3]).max()
    check.equal(actual, 3)


def test_count():
    actual = I([1, 2, 3]).count()
    check.equal(actual, 3)


def test_len():
    actual = I([1, 2, 3]).len()
    check.equal(actual, 3)


def test_find():
    actual = I([1, 2, 3]).find(lambda item: item == 2)
    check.equal(actual, 2)


def test_all():
    actual = I([1, 2, 3]).all(lambda item: item == 2)
    check.is_false(actual)


def test_any():
    actual = I([1, 2, 3]).any(lambda item: item == 2)
    check.is_true(actual)


def test_last():
    actual = I([1, 2, 3]).last()
    check.equal(actual, 3)


def test_zip():
    actual = I([1, 2, 3]).zip([4, 5, 6]).list()
    check.equal(actual, [(1, 4), (2, 5), (3, 6)])


def test_unzip():
    actual = I([(1, 4), (2, 5), (3, 6)]).unzip().list()
    check.equal(actual, [(1, 2, 3), (4, 5, 6)])


def test_skip():
    actual = I([1, 2, 3]).skip(1).list()
    check.equal(actual, [2, 3])


def test_take():
    actual = I([1, 2, 3]).take(2).list()
    check.equal(actual, [1, 2])


def test_flatten():
    actual = I([[1, 4], [2, 5], [3, 6]]).flatten().list()
    check.equal(actual, [1, 4, 2, 5, 3, 6])


def test_chain():
    actual = I([1, 2, 3]).chain([4, 5, 6]).list()
    check.equal(actual, [1, 2, 3, 4, 5, 6])


def test_fill():
    actual = I([1, 2, 3]).fill(4).list()
    check.equal(actual, [4, 4, 4])


def test_reverse():
    actual = I([1, 2, 3]).reverse().list()
    check.equal(actual, [3, 2, 1])


def test_sum():
    actual = I([1, 2, 3]).sum()
    check.equal(actual, 6)


def test_product():
    actual = I([1, 2, 3]).product()
    check.equal(actual, 6)


def test_permutations():
    actual = I([1, 2, 3]).permutations(2).list()
    check.equal(actual, [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])


def test_position():
    actual = I([1, 2, 3]).position(lambda item: item == 2)
    check.equal(actual, 1)


def test_sort():
    actual = I([2, 1, 3]).sort()
    check.equal(actual, [1, 2, 3])


def test_first():
    actual = I([2, 1, 3]).first()
    check.equal(actual, 2)
