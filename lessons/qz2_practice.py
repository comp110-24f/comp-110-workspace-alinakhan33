# odd_and_even


def odd_and_even(lst: list[int]) -> list[int]:
    """Find the odd elements with even indexes"""
    idx: int = 0
    lst2: list[int] = []

    while idx < len(lst):
        if lst[idx] % 2 == 1 and idx % 2 == 0:
            lst2.append(lst[idx])
        idx += 1
    return lst2


# short words
def short_words(lst: list[str]) -> list[str]:
    """Returns list of words that are shorter than 5 characters"""
    new_list: list[str] = []
    for elem in lst:
        if len(elem) < 5:
            new_list.append(elem)
        else:
            print(f"{elem} is too long!")
    return new_list


# multiples
def multiples(lst: list[int]) -> list[bool]:
    """whether each int value is a multiple of the previous value"""
    mults: list[bool] = []
    # check first value against last value
    # a is a multiple of b means a % b == 0
    mults.append(lst[0] % lst[len(lst) - 1] == 0)
    # start at idx 1 since we already used idx 0
    idx: int = 1
    while idx < len(lst):
        # a is a multiple of b means a % b == 0
        mults.append(lst[idx] % lst[idx - 1] == 0)
        idx += 1
    return mults

# dictionaries
# value_exists
def value_exists(d: dict[str, int], num: int) -> bool:
    for key in d:
        if d[key] == num:
            return True
    return False

# plus_or_minus_n
def plus_or_minus_n(inp: dict[str,int], n: int) -> None:
    for key in inp:
        if inp[key] % 2 == 0:
            inp[key] = inp[key] + n
        else: # element is odd
            inp[key] = inp[key] - n

# free_biscuits
def free_biscuits(input: dict[str, list[int]]) -> dict[str, bool]:
    result: dict[str, bool] = {}
    #loop over each key in my input dict
    for key in input:
        # 

# For loops code rewrite
stats: list[int] = [7, 8, 9]
total: int = 100
for elem in stats:
    total -= elem

# for in loops
stats: list[int] = [7,8,9]
total: int = 100
for index in range(0, len(stats)):
    total -= stats[index]