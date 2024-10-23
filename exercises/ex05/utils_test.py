"""Exercise #05 Unit Test COMP110!"""

__author__ = "730485036"

import pytest
from exercises.ex05.utils import only_evens, sub, add_at_index


# only_evens test -> edge case 1st and then 2 use cases
# edge case
def test_only_evens_edge() -> None:
    """only_evens should return an empty list when given an empty input"""
    assert only_evens([]) == []


# use case 1
def test_only_evens_use_1() -> None:
    """only_evens should return even numbers from list of mixed numbers"""
    assert only_evens([1, 2, 3, 4, 5, 6, 7, 8]) == [2, 4, 6, 8]


# use case 2
def test_only_evens_use_2() -> None:
    """only_evens should return an empty list if all the numbers are odd"""
    assert only_evens([3, 1, 7, 5, 9]) == []


# sub test -> edge case 1st and then 2 use cases
# edge case
def test_sub_edge() -> None:
    """if the input is empty, sub should return an empty list"""
    assert sub([], 0, 1) == []


# use case 1
def test_sub_use_1() -> None:
    """sub should return correct subset list"""
    assert sub([10, 20, 30, 40, 50], 1, 4) == [20, 30, 40]


# use case 2
def test_sub_use_2() -> None:
    """sub should properly adjust indices out of bounds"""
    assert sub([10, 20, 30], -5, 10) == [10, 20, 30]


# add_at_index test -> edge case 1st and then 2 use cases
# edge case
def test_add_at_index_edge() -> None:
    """add_at_index should raise an IndexError"""
    testing: list[int] = [1, 2, 3]
    with pytest.raises(IndexError):
        add_at_index(testing, 0, 5)


# use case 1
def test_add_at_index_use_1() -> None:
    """add_at_index adds an element to the beginning of the list"""
    testing: list[int] = [2, 3, 4]
    add_at_index(testing, 1, 0)
    assert testing == [1, 2, 3, 4]


# use case 2
def test_add_at_index_use_2() -> None:
    """add_at_index inserts an element to the middle of the list"""
    testing: list[int] = [1, 2, 4, 5]
    add_at_index(testing, 3, 2)
    assert testing == [1, 2, 3, 4, 5]
