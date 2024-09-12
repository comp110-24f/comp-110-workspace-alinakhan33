"""Writing a program to help me plan a tea party including the amount of guests and cost of supplies."""

__author__ = "730485036"

"""Keep pushing changes to git!"""


def main_planner(guests: int) -> None:
    """This function brings every function below together"""
    """Using variables to calculate # of tea bags and treats based on # of guests"""
    tea_bag_num: int = tea_bags(people=guests)
    treats_num: int = treats(people=guests)
    """Now find the total cost of items"""
    total: float = cost(tea_count=tea_bag_num, treat_count=treats_num)


main_planner(guests=2)

print("A Cozy Tea Party for " + str(guests) + "People!")
print("Tea Bags: " + str(tea_bag_num))
print("Treats: " + str(treats_num))
print("Cost: $" + str(total_cost))


def tea_bags(people: int) -> int:
    """How many tea bags we need based on num of people attending"""
    return people * 2


tea_bags(people=2)


def treats(people: int) -> int:
    """Num of treats is 1.5x the num of teas"""
    return int(tea_bags(people=people) * 1.5)
    """The data type must return as an int"""


treats(people=2)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculate the cost of treats and tea bags combined, return type is float"""
    teabag_cost: float = tea_count * 0.5
    treat_cost: float = treat_count * 0.75
    """Use variables to create a set cost of 50 cents per tea bag and 75 cents per treat"""
    return teabag_cost + treat_cost


cost(tea_count=2, treat_count=6)
