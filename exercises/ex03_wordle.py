"""EX03 - My secret_wordle game!"""

__author__ = "730485036"
# remember to push changes


def main(secret_word: str) -> None:
    """The entrypoint of the program and main game loop."""
    secret_word_len: int = len(secret_word)
    turn: int = 1  # Starting with the 1st turn

    # The game will loop while the number of turns is 6 or below
    while turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(secret_word_len)  # Get player's guess
        print(emojified(guess, secret_word))

        # Is the guess correct?
        if guess == secret_word:
            print(f"You won in {turn}/6 turns!")
            return
        else:
            turn += 1  # Onto the next turn

    # User fails the wordle past 6 turns
    if turn > 6:
        print("X/6 - Sorry, try again tomorrow!")


def input_guess(secret_word_len: int) -> str:
    """Function checks if user input secret_word's num of characters matches secret_word"""
    while True:
        guess = input(f"Enter a {secret_word_len} character word: ")
        if len(guess) == secret_word_len:
            return guess
        else:
            print(f"That wasn't {secret_word_len} chars! Try again: {guess}")


# print(input_guess(secret_word_len=5))


# Part 2
def contains_char(secret_word: str, char_guess: str) -> bool:
    """See if a specific character is in the given secret_word"""
    assert len(char_guess) == 1
    index: int = 0

    # Check each index of secret_word
    while index < len(secret_word):
        if secret_word[index] == char_guess:
            return True
        index += 1  # check the next character
    return False


# print(contains_char(secret_word="abcde", char_guess="o"))


def emojified(guess: str, secret_word: str) -> str:
    """Using emojis to represent accuracy of guess by comparing two strings"""
    assert len(guess) == len(secret_word)

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    result: str = ""
    index: int = 0

    while index < len(guess):
        if guess[index] == secret_word[index]:
            result += GREEN_BOX  # Correct letter + location
        elif contains_char(secret_word, guess[index]):
            result += YELLOW_BOX  # Correct letter but wrong location
        else:
            result += WHITE_BOX  # Letter not found in secret word
        index += 1
    return result


# print(emojified(guess="hello", secret_word="world"))

if __name__ == "__main__":
    main(secret_word="table")
