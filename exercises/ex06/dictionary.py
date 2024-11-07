"""Exercise #06 COMP110!"""

__author__ = "730485036"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Function inverts the keys and the values."""
    inverted: dict[str, str] = dict()
    for values in input_dict:
        if input_dict[values] in inverted:
            raise KeyError("Error: Duplicate key")
        else:
            inverted[input_dict[values]] = values
    return inverted


def favorite_color(colors: dict[str, str]) -> str:
    """Returns str of the most popular color"""
    popular: str = ""
    new_colors: dict[str, int] = dict()
    idx: int = 0
    # count frequency of each color
    for c in colors:
        if colors[c] in new_colors:  # check if color is already in new_colors
            new_colors[colors[c]] += 1
        else:
            new_colors[colors[c]] = 1  # Back to 1 if it doesn't exist
    for count in new_colors:
        if new_colors[count] > idx:  # is the current color's count the highest so far?
            idx = new_colors[count]  # update highest count
            popular = count  # set to most popular color
    return popular


def count(freq: list[str]) -> dict[str, int]:
    """Given a list, the function produces a dict where each key is unique and each value is the count of # of times the value appeared in input"""
    new: dict[str, int] = dict()
    for x in freq:
        if x in new:
            new[x] += 1
        else:
            new[x] = 1
    return new


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Categorizes words by their starting letter."""
    result: dict[str, list[str]] = {}

    # Iterate over each word in the input list
    for word in words:
        first_letter: str = word[0].lower()  # Get the first letter in lowercase

        # Add the word to the list in the dict
        if first_letter in result:
            result[first_letter].append(word)
        else:
            result[first_letter] = [word]  # start a new list for this letter

    return result


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    """Updates the attendance sheet with the new student entry and avoids duplicates."""

    # If the day exists, ensure the student isn't already in the list
    if day not in attendance:

        attendance[day] = []
    if student not in attendance[day]:
        attendance[day].append(student)  # Adding student after accessing list
