"""Basic syntax of lists"""

# Create an empty list
my_numbers: list[float] = []  # literal
my_numbers: list[float] = list()  # constructor

print(my_numbers)

# String Analogy
# my_name: str = ""  # literal
# my_name: str = str()  # constructor

# Adding a value to a list
my_numbers.append(1.5)
my_numbers.append(2.3)
print(my_numbers)

# Creating an already populated list
game_points: list[int] = [102, 86, 94]
print(game_points)

# Subscription Notation/Indexing
print(game_points[2])
last_game: int = game_points[2]
print(last_game)
