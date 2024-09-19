"""Challenge Question #03 COMP110!"""

__author__ = "730485036"


def num_instances(phrase: str, search_char: str) -> int:

    # increase this everytime an instance of search_char is found
    count: int = 0

    # track index so i can loop over every element of phrase
    index: int = 0

    # loop through every charater in the phrase
    while index < len(phrase):

        # check if the selected character matches search_char
        if phrase[index] == search_char:
            count = count + 1
        index = index + 1
    return count
