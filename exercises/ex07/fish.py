"""File to define Fish class."""

__author__ = "730485036"


class Fish:
    """Class of Fish."""

    age: int

    def __init__(self):
        """Initialize the fish class."""
        self.age = 0
        return None

    def one_day(self):
        """Increase the fish's life."""
        self.age += 1
        return None
