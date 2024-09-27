def remove_chars(msg: str, char: str) -> str:
    """Return a copy of msg with all instances of char removed."""
    copy: str = ""  # set up empty str to copy values over
    index: int = 0
    while index < len(msg):
        # if the letter is NOT char
        if not (msg[index]) == char:  # if msg[index] != char
            copy += msg[index]  # copy = copy + msg[index]
        index += 1
    return copy


word: str = "yoyo"  # GLOBAL variable

print(remove_chars(word, char="y"))  # with keyword arguments

# print(remove_chars(word, "o"))  with positional arguments
