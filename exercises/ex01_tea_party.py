"""Writing a program to help me plan a tea party"""

__author__ = "730485036"

"""Keep pushing changes to git!"""


def tea_bags(people: int) -> int:
    """How many tea bags we need based on num of people attending"""
    return people * 2


tea_bags(people=2)


def treats(people: int) -> int:
    """Num of treats is 1.5x the num of teas"""
    return int(tea_bags(people=people) * 1.5)
    """The data type must return as int"""


treats(people=2)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculate the cost of treats and tea bags combined, return type is float"""
    teabag_cost = tea_count * 0.5
    treat_cost = treat_count * 0.75
    return teabag_cost + treat_cost


cost(tea_count=2, treat_count=6)
