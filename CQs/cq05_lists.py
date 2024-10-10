"""Mutating functions."""

_author_ = "730485036"


def manual_append(a: list[int], b: int) -> None:
    a.append(b)


def double(a: list[int]) -> None:
    idx: int = 0
    while idx < len(a):
        a[idx] *= 2
        idx += 1


list1: list[int] = [1, 2, 3]
list2: list[int] = list1

double(a=list2)

print(list1)
print(list2)
