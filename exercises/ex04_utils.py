"""list Utility Functions exercise #4"""

_author_ = "730485036"


def all(lst: list[int], num: int) -> bool:
    # Loop thru list elements
    for x in range(0, len(lst)):
        if lst[x] != num:
            return False
    # If the elements match
    return True


# Max function returns largest in the list
def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    max_num: int = input[0]
    # iterate thru inputted list to see if an element is greater than the max num
    for elem in input:
        if elem > max_num:
            max_num = elem  # If elem is greater, set it as the max number
    return max_num


def is_equal(list1: list[int], list2: list[int]) -> bool:
    if list1 == list2:
        return True
    else:
        return False


def extend(list1: list[int], list2: list[int]) -> None:
    for elem in list2:  # loop through each item in list
        list1.append(elem)  # add items from second list to first list
