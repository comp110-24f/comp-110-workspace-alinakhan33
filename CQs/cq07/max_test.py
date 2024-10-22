"""Unit Tests for Challenge Question #07 COMP110!"""

__author__ = "730485036"

from CQs.cq07.find_max import find_and_remove_max


def test_get_first_use_case() -> None:
    """Ensures find_and_remove_max returns the expected value."""
    assert find_and_remove_max([3, 8, 9, 2, 1]) == 9


def test_get_second_use_case() -> None:
    """Ensures find_and_remove_max mutates the input in the expected way."""
    input: list[int] = [4, 5, 6, 7]
    find_and_remove_max(input)
    assert input == [4, 5, 6]


def test_get_third_use_case() -> None:
    """ensures find_and_remove_max returns the correct value in case of an unconventional input."""
    input: list[int] = []
    assert find_and_remove_max(input) == -1
    assert input == []


def test_get_fourth_use_case() -> None:
    """ensures find_and_remove_max returns the correct value in case of an unconventional input."""
    input: list[int] = [7, 7, 7]
    assert find_and_remove_max(input) == 7
    assert input == []
