"""Writing a program to help me plan a tea party including the amount of guests and cost of supplies."""

__author__ = "730485036"

"""Keep pushing changes to git!"""


def main_planner(guests: int) -> None:
    """This function brings every function below together"""
    """Using variables to calculate # of tea bags and treats based on # of guests"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """How many tea bags we need based on num of people attending"""
    return people * 2


def treats(people: int) -> int:
    """Num of treats is 1.5x the num of teas"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculate the cost of treats and tea bags combined, return type is float"""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
