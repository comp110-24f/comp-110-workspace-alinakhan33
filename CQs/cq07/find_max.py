"""Challenge Question #07 COMP110!"""

__author__ = "730485036"


def find_and_remove_max(input: list[int]) -> int:

    # if the list is empty, return -1
    if len(input) == 0:
        return -1

    largest_num: int = input[0]

    for elem in input:
        if elem > largest_num:
            largest_num = elem
    # Remove all instances of the largest number in the input list
    idx: int = 0
    while idx < len(input):
        if input[idx] == largest_num:
            input.pop(idx)
        else:
            idx += 1
    return largest_num
