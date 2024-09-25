"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730485036"


def main() -> None:
    contains_char(
        word=input_word(), letter=input_letter()
    )  # pulling previous step functions into this function


# Prompting for an Input Word
def input_word() -> str:
    # Gather user input
    word: str = str(input("Enter a 5-character word: "))
    # Create an if statement to test if the user input is 5 characters, if not, print an error msg
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    return word


# Prompting for an Input Character
def input_letter() -> str:
    # Create an if statement to test if the user input is one character
    letter: str = str(input("Enter a single character: "))
    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    return letter


def contains_char(word: str, letter: str) -> None:
    word = word  # assigning parameters to local variables
    letter = letter
    count: int = 0

    # Filter thru each index to see if the character's in the word
    print("Searching for " + str(letter) + " in " + str(word))
    if letter == word[0]:
        print(str(letter) + " found at index 0")
        count = count + 1
    if letter == word[1]:
        print(str(letter) + " found at index 1")
        count = count + 1
    if letter == word[2]:
        print(str(letter) + " found at index 2")
        count = count + 1
    if letter == word[3]:
        print(str(letter) + " found at index 3")
        count = count + 1
    if letter == word[4]:
        print(str(letter) + " found at index 4")
        count = count + 1
    # Print number of matches
    if count > 1:
        print(str(count) + " instances of " + letter + " found in " + word)
    if count == 1:
        print(str(count) + " instance of " + letter + " found in " + word)
    if count < 1:
        print("No instances of " + letter + " found in " + word)


if __name__ == "__main__":
    main()
