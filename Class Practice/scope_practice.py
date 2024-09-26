def remove_chars(msg: str, char: str) -> str:
    """Return a copy of msg with all instances of char removed."""
    copy: str = "" # set up empty str to copy values over
    index: int: 0
    while index < len(msg):
        # if the letter is NOT char
        if not (msg[index]) != char: # msg[index] != char
            # add it to copy
            copy += msg[index] # copy = copy + msg[index]
        index += 1 # index = index + 1
    return copy


# remove_chars(msg="football", char="o") -> "ftball"