"""Coordinates File."""

__author__ = "730485036"


def get_coords(xs: str, ys: str) -> None:
    index: int = 0
    while index < len(xs):
        another_index = 0
        while another_index < len(ys):
            print(xs[index], ys[another_index])
            another_index += 1
        index += 1


get_coords("12", "34")
