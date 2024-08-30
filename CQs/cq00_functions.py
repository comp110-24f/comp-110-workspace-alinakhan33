"""Challenge Question #1 COMP110!"""

__author__ = "730485036"


def mimic(message: str) -> str:
    """This function takes your input and repeats it."""
    return message


def main() -> None:
    """This function prints the result of calling mimic"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
