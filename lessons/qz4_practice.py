"""Quiz #4 Practice."""


# 1
class Course:
    """Models the idea of a UNC course."""

    name: str
    level: int
    prerequisites: list[str]

    def is_valid_course(self, prereq: str) -> bool:
        """If course is > 400 and in prereq list."""
        results: bool = False
        if self.level < 400:
            return False
        else:
            for p in self.prerequisites:
                if p == prereq:
                    return True
            return False


def find_courses(lst: list[Course], prereq: str) -> list[str]:
    """Prereqs over 400+."""
    results: list[str] = []
    for c in lst:
        if c.level >= 400:
            for p in c.prerequisites:
                if p == prereq:
                    results.append(c.name)
    return results


class Car:
    """Represents basic model of a car."""

    make: str
    model: str
    year: int
    color: str
    mileage: float

    def __init__(self, make: str, model: str, year: int, color: str, mileage: float):
        """Initialize all attributes."""
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mileage = mileage

    def update_mileage(self, miles: float) -> None:
        """Updates mileage."""
        self.mileage += miles

    def display_info(self) -> None:
        """Print all attributes."""
        print(
            f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Color: {self.color}, Mileage: {self.mileage}"
        )


def calculate_depreciation(vehicle: Car, depreciation_rate: float) -> float:
    """Calculates depreciation of car value."""
    return vehicle.mileage * depreciation_rate


class HotCocoa:
    """Hot Cocoa."""

    has_whip: bool
    flavor: str
    marshmallow_count: int
    sweetness: int

    def __init__(
        self, has_whip: bool, flavor: str, marshmallow_count: int, sweetness: int
    ):
        """Initialize all attributes."""
        self.has_whip = has_whip
        self.flavor = flavor
        self.marshmallow_count = marshmallow_count
        self.sweetness = sweetness

    def mallow_adder(self, mallows: int) -> int:
        self.marshmallow_count += mallows
        self.sweetness += mallows * 2

    def __str__(self) -> str:
        if self.has_whip:
            return f"A {self.flavor} cocoa with whip, {self.marshmallow_count} marshmallows, and level {self.sweetness} sweetness."
        else:
            return f"A {self.flavor} cocoa without whip, {self.marshmallow_count} marshmallows, and level {self.sweetness} sweetness."


def order_cost(objects: list[HotCocoa]) -> float:
    cost: float = 0.0
    for x in objects:
        if x.has_whip:
            cost += 2.50
        else:
            cost += 2.00
    return cost


my_order: HotCocoa = HotCocoa(False, "vanilla", 5, 2)
my_order.has_whip = True
my_order.mallow_adder(2)
viktoryas_order: HotCocoa = HotCocoa(True, "peppermint", 10, 2)
order_cost([my_order, viktoryas_order])
print(my_order)


class TimeSpent:
    """Time spent."""

    name: str
    purpose: str
    minutes: int

    def __init__(self, name: str, purpose: str, minutes: int):
        self.name = name
        self.purpose = purpose
        self.minutes = minutes

    def add_time(self, time: int) -> None:
        self.minutes += time

    def __add__(self, added_minutes: int) -> TimeSpent:
        return TimeSpent(self.name, self.purpose, self.minutes + added_minutes)

    def reset(self) -> None:
        old_value: int = self.minutes
        self.minutes = 0
        return old_value

    def __str__(self) -> str:
        minutes: int = self.time % 60
        hours: int = (self.time - minutes) / 60
        return (
            f"{self.name} has spent {hours} hours and {minutes} minutes on screen time"
        )


def most_by_purpose(lst: list[TimeSpent], activity: str) -> str:
    max_time: int = 0
    max_name: str = ""
    for elem in times:
        if (elem.purpose == activity) and (elem.minutes > max_time):
            max_time = elem.minutes
            max_name = elem.name
    return max_name


# 1
def factorial(n: int):
    if n == 0:
        return 1
    return n * factorial(n - 1)


# 2
def sum_of_natural_numbers(n: int):
    if n == 0:
        return 0
    return n + sum_of_natural_numbers(n - 1)


# 3
def sum_of_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)


# 4
def power(num: int, exponent: int):
    if exponent == 0:
        return 1
    return num * power(num, exponent - 1)


# 6 reverse string
def reverse_string(s: str):
    return reverse_helper(s, len(s) - 1)


def reverse_helper(s, index):
    if index < 0:
        return ""
    return s[index] + reverse_helper(s, index - 1)


# Base case: No more integers left
# Recursive case: total sum of all integers in linked list


from __future__ import annotations


class Node:
    def __init__(self, value: list[int], next: Node | None):
        self.value = value  # A list of integers
        # Either another Node or None
        if next is None:
            self.next = None
        else:
            self.next = next


def sum_node_values(head: Node | None) -> int:
    """Sum of all integers in linked list."""
    if head is None:
        return 0  # Base case: nothing left in linked list

    # Recursive step: sum of the elements of the current node and the sum of the rest of the list
    current_sum = 0
    for value in head.value:
        current_sum += value
    return current_sum + sum_node_values(head.next)


def increment_node_values(head: Node | None):
    """Increment every integer in every node's list by 1"""
    # Base case: end of list
    if head is None:
        return 0
    # Recursive case: increment each value in the current node
    for i in range(len(head.value)):  # Manually increment each element
        head.value[i] += 1
    increment_node_values(head.next)  # Onto the next node


def __str__(self) -> str:
    return str(self.value)


def print_nodes(head: Node | None) -> None:
    if head is None:
        return None  # Base case

    # Recursive case: Print the current node and then the rest of the list
    print(head)  # Use the __str__ method to get the str representation
    print_nodes(head.next)


# 2
from __future__ import annotations


class BinaryTreeNode:
    def __init__(
        self, value: int, left: BinaryTreeNode | None, right: BinaryTreeNode | None
    ):
        self.value = value  # Integer value of the node
        if left is None:
            self.left = None
        else:
            self.left = left

        if right is None:
            self.right = None
        else:
            self.right = right


def sum_tree_values(root: BinaryTreeNode | None) -> int:
    """Binary tree."""
    # Base case: end of the list, no more values left
    if root is None:
        return 0

    # Recursive case: Return total sum of all values in the trees (add the value, left and right)
    return root.value + sum_tree_values(root.left) + sum_tree_values(root.right)


def increment_tree_values(root: BinaryTreeNode | None) -> None:
    # Base case: end of the list, no more values left
    if root is None:
        return 0

    # Recursive case: increment the value of each node in tree by 1
    # Start with current value
    root.value += 1

    # Keep moving in the list
    increment_tree_values(root.left)
    increment_tree_values(root.right)
