"""Visualize File."""

__author__ = "730485036"

# import concat function from concatenation.py
from CQs.cq04.concatenation import concat
from CQs.cq04.coordinates import get_coords

x: str = "123"
y: str = "abc"

# Call the function
if __name__ == "__main__":
    print(concat(x, y))
    get_coords(x, y)
