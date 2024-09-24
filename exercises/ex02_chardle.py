"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730485036"

# Comment on code and push changes


# Prompting for an Input Word
def input_word() -> str:
    # Gather user input
    get_input: str = str(input("Enter a 5-character word: "))

    # Create an if-else statement to test if the user input is 5 characters, if not, print an error msg
    if len(get_input) == 5:
        print(get_input)
    else:
        print("Error: Word must contain 5 characters.")

    return get_input


input_word()


# Prompting for an Input Character
def input_letter() -> str:
    get_char_input: str = str(input(("Enter a single character: ")))

    # Create an if-else statement to test if the user input is one character
    if len(get_char_input) == 1:
        print(get_char_input)
    else:
        print("Error: You must enter exactly one character.")
    return get_char_input


input_letter()
