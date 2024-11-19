"""EX08 COMP 110."""

from __future__ import annotations

__author__ = "730485036"


class Node:
    """Node class."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        """Initializer."""
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Produce a string representation of a linked list."""
        rest: str = "TODO"
        # TODO: Figure out the rest of the list
        if self.next is None:  # Base case
            rest = "None"
        else:  # Recursive case
            rest = str(self.next)
        return f"{self.value} -> {rest}"


two: Node = Node(2, None)
one: Node = Node(1, two)
courses: Node = Node(110, Node(210, Node(301, None)))

# Be sure to get here!


def to_str(head: Node | None) -> str:
    """Represent a Linked List as a str."""
    if head is None:
        return "None"
    else:
        rest: str = to_str(head.next)
        return f"{head.value} -> {rest}"


def last(head: Node) -> int:
    """Return the last value of a non-empty list."""
    # Base Case: when head is the last node
    # return its value !
    # Recursive case:
    # Figure out the last node (recursive call)
    # in the "rest of the list"
    # Return this value!
    return -1


def value_at(head: Node | None, index: int) -> int:
    """Return the value at the given index of the linked list."""
    if head is None:  # Edge case: empty list or index out of bounds
        raise IndexError("Index is out of bounds on the list.")
    if index == 0:  # Base case: if index is 0
        return head.value
    return value_at(
        head.next, index - 1
    )  # Recursive case: move to the next node and decrement the index
    # When u move to next node, the index decreases to reflect the remaining distance to the target position


def max(head: Node | None) -> int:
    """Return the maximum value in the linked list."""
    if head is None:  # Edge case: linked list is empty
        raise ValueError("Cannot call max with None")

    if head.next is None:  # Base case: There's only one node
        return head.value

    # Recursive case: find the max val in the rest of the list
    maximum = max(head.next)
    if head.value > maximum:
        return head.value
    else:
        return maximum


def linkify(items: list[int]) -> Node | None:
    """Return a Linked List of Nodes with the same values."""
    if len(items) == 0:  # empty list
        return None
    # Create a Node for the first item and link the rest
    return Node(items[0], linkify(items[1:]))


def scale(head: Node | None, factor: int) -> Node | None:
    """Return a new linked list where each value is multiplied by the scaling factor."""
    if head is None:  # if the list is empty
        return None

    # Recursive case: create a new node with scaled value and link it to the rest
    return Node(head.value * factor, scale(head.next, factor))
