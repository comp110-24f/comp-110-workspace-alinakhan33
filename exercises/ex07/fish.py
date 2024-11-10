"""File to define Fish class."""


class Fish:
    age: int

    def __init__(self):
        self.age = 0
        return None

    def one_day(self):
        """Increase the fish's life"""
        self.age += 1
        return None
