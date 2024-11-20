"""Exploring linked list utils in class."""

from __future__ import annotations


class Node:
    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
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
print(one)
print(str(courses))
print(courses)
# Be sure to get here!


def to_str(head: Node | None) -> str:
    """Represent a Linked List as a str."""
    if head is None:
        return "None"
    else:
        rest: str = to_str(head.next)
        return f"{head.value} -> {rest}"


print(to_str(one))
print(to_str(courses))


def last(head: Node) -> int:
    """Return the last value of a non-empty list"""
    # Base Case: when head is the last node
    # return its value !
    # Recursive case:
    # Figure out the last node (recursive call)
    # in the "rest of the list"
    # Return this value!
    return -1


print(last(one))  # Expect to print 2
print(last(courses))  # Expect to print 301


def recursive_range(start: int, end: int) -> Node | None:
    """Build a list recursively from start to end."""

    # TODO: Can you handle an edge case? What is it?
    # if so, raise ValueError("invalid arguments")

    if start > end:
        raise ValueError("Invalid arguments, start > end")

    if start == end:  # Base case
        return None
    else:
        # Recursive case
        # Handle the first value in your new list here
        first: int = start
        # 2. let the rest of the list be handled recursively
        rest: Node | None = recursive_range(start + 1, end)
        # 3. Return a new node which is first followed by rest
        return Node(first, rest)


a_list: Node | None = recursive_range(110, 150)
print(a_list)
