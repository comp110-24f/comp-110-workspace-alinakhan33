"""Concatenation File."""

__author__ = "730485036"


# Concat function that takes two str params
def concat(str1: str, str2: str) -> str:
    return str1 + str2


# Global variables (will be outside of function)
word1: str = "happy"
word2: str = "tuesday"

print(concat(word1, word2))
