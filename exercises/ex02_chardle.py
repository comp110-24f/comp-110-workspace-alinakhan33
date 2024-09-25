"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730485036"

# Comment on code and push changes


def main() -> None:

    # Prompting for an Input Word
    def input_word() -> str:
        # Gather user input
        word: str = str(input("Enter a 5-character word: "))

        # Create an if-else statement to test if the user input is 5 characters, if not, print an error msg
        if len(word) == 5:
            print(word)
        else:
            print("Error: Word must contain 5 characters.")
            exit()
        return word

    # Prompting for an Input Character
    def input_letter() -> str:
        letter: str = str(input(("Enter a single character: ")))

        # Create an if-else statement to test if the user input is one character
        if len(letter) == 1:
            print(letter)
        else:
            print("Error: You must enter exactly one character.")
            exit()
        return letter

    def contains_char(word: str, letter: str) -> None:

        print("Searching for " + letter + " in " + word)

        letter_instance: int = 0

        # Filter thru each index to see if the character's in the word
        if word[0] == letter:
            print(str(letter) + " found at index 0")
            letter_instance += 1
        if word[1] == letter:
            print(str(letter) + " found at index 1")
            letter_instance += 1
        if word[2] == letter:
            print(str(letter) + " found at index 2")
            letter_instance += 1
        if word[3] == letter:
            print(str(letter) + " found at index 3")
            letter_instance += 1
        if word[4] == letter:
            print(str(letter) + " found at index 4")
            letter_instance += 1
        # Print number of matches
        if letter_instance > 0:
            print(
                str(letter_instance) + " instances of " + letter + " found in " + word
            )
        else:
            print("No instances of " + letter + " found in " + word)

    contains_char(word=input_word(), letter=input_letter())


main()
