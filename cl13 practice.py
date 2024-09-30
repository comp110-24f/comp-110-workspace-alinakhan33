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

print(game_points[2])
print(game_points[len(game_points) - 1])

# Subscription Notation/Indexing
print(game_points[2])
last_game: int = game_points[2]
print(last_game)

# Modifying by Index
# (because lists are mutable)
game_points[1] = 72
print(game_points)

class: str = "110" # change it to "210"
class_num[0] = "2"

# Getting the length
len(game_points)

# Removing an Item
game_points.pop(1)
print(game_points)

# Function name: display
# Parameter: list of integers
# RV: None
# Print every element in the input list
# Call display on game_points