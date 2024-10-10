"""Summing the elements of a list using different loops"""

_author_ = "730485036"


def w_sum(vals: list[float]) -> float:
    idx: int = 0
    sum: float = 0
    while idx < len(vals):
        sum += vals[idx]
        idx += 1
    return sum


def f_sum(vals: list[float]) -> float:
    sum: float = 0
    for x in vals:
        sum += x
    return sum


def f_range_sum(vals: list[float]) -> float:
    sum: float = 0
    for x in range(0, len(vals)):
        sum += vals[x]
    return sum
