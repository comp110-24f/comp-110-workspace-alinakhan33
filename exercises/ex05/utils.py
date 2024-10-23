"""Exercise #05 COMP110!"""

__author__ = "730485036"


# First function
def only_evens(values: list[int]) -> list[int]:
    result: list[int] = []
    for elem in range(len(values)):
        # Testing if its even
        if values[elem] % 2 == 0:
            result.append(values[elem])
    return result


# Second function
def sub(values: list[int], start: int, end: int) -> list[int]:
    # special cases
    if len(values) == 0 or start >= len(values) or end <= 0:
        return []

    # if start is negative
    if start < 0:
        start = 0
    if end > len(values):
        end = len(values)

    # Build subset list
    result: list[int] = []
    for elem in range(start, end):
        result.append(values[elem])
    return result


# Third function
def add_at_index(values: list[int], element: int, idx: int) -> None:
    # is the index out of range?
    if idx < 0 or idx > len(values):
        raise IndexError("Index is out of bounds for the input list")
    # appending something to the list
    values.append(0)

    # Make space and shift elements to the right
    for elem in range(len(values) - 1, idx, -1):
        values[elem] = values[elem - 1]
    # Insert new element at specific index
    values[idx] = element
