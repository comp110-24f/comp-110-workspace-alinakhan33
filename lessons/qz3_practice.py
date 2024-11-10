# how you remove a key-value pair to a dictionary object.

# <object_variable>.pop(<key>)
my_dict = {"name": "Alice", "age": 25}
# Create a new key-value pair using the value from the old key
my_dict["years_old"] = my_dict.pop("age")
print(my_dict)

# <object_variable>[<key>] = <value>
my_dict = {"name": "Alice", "age": 25}
my_dict["location"] = "New York"  # Adds a new key-value pair to the dictionary
print(my_dict)
# Output: {"name": "Alice", "age": 25, "location": "New York"}

# Create a new dictionary called my_dictionary with str keys and float values and initialize it as an empty dictionary
# Access value under "Yall"
my_dictionary: dict[str, float] = {}
msg: dict[str, int] = {"Hello": 1, "Yall": 2}
msg["Yall"]
# Increase value stored under "Yall" by 3
msg["Yall"] += 3

# Remove value "Alyssa" stored at Key 100
ids: dict[int, str] = {100: "Alyssa", 200: "Carmine"}
ids.pop(100)
# get the number of key/value pairs in the dictionary
len(ids)

# add new key-value pair
inventory: dict[str, int] = {"pens": 10, "notebooks": 5, "erasers": 8}
inventory["markers"] = 15

# update value of "milk" to 2.50
prices: dict[str, float] = {"bread": 2.99, "milk": 1.99, "eggs": 3.49}
prices["milk"] = 2.50

# print out all keys in the dict
scores: dict[str, int] = {"Alice": 85, "Bob": 90, "Charlie": 88}
for x in scores:
    print(x)
# return sum of the values (scores) assuming there's a sum function
total_score = sum(scores)
# assume that the only parameter in the sum function is inp_dict
total_score = sum(inp_dict=scores)

# iterate over key-value pairs and print them in the format "key: value"
fruit_count: dict[str, int] = {"apples": 5, "bananas": 8}
for key in fruit_count:
    value = fruit_count[key]
    print(f"{key}: {value}")

# combine 2 dictionaries
combo_dict: dict[str, int] = {"a": 1, "b": 2, "c": 3, "d": 4}

# Lists, Dictionaries, and Loops Reinforcement Questions
# 1
my_list: list[int] = list()
# 1a. Add the numbers 8, 0, 3, and -1 to the list.
my_list.append(8)
my_list.append(0)
my_list.append(3)
my_list.append(-1)
# 1b. Remove the number 3 from the list.
my_list.pop(3)
# 1c. Assign the element at the second index to a variable named 'dog'.
dog = my_list[2]
# 1d. Print the number of items in the list.
print(len(my_list))
# 1e. Change the value 8 to 0.
my_list[0] = 0
# 1f. Instantiate a list[int] with the first value returned from calling sum on my_list.
summed_list: list[int] = [sum(my_list)]

# 2
my_dict: dict[int, str] = {}
# 2a. Add key-value pairs to the dictionary.
my_dict[8] = "eight"
my_dict[0] = "zero"
my_dict[3] = "three"
my_dict[-1] = "negative one"
# 2b. Remove the key-value pair where the value is 'three'
my_dict.pop(3)
# 2c. Assign the value associated with the key 0 to a variable called 'cat'.
cat = my_dict[0]
# 2d. Print the number of keys in the dictionary.
print(len(my_dict))
# 2e. Print the number of values in the dictionary.
print(len(my_dict))
# 2f. Change the value associated with the key 8 to 'zero'.
my_dict[8] = "zero"
# 2g. Instantiate a dict[str, int] with the key 'returned_amount' and the value from sum_dict_keys(my_dict).
new_dict: dict[str, int] = {"returned_amount": sum_dict_keys(my_dict)}

# 3
my_dict: dict[int, str] = {0: "dog", 1: "cat", 2: "mouse", 3: "bird", 4: "whale"}
# 3a.
for x in range(0, len(my_dict)):
    print(my_dict[x])
# Output: dog, cat, mouse, bird, whale

# 3b.
for x in range(0, len(my_dict)):
    print(x)
# Output: 0, 1, 2, 3, 4

# 3c.
for x in my_dict:
    print(my_dict[x])
# Output: dog, cat, mouse, bird, whale

# 3d.
for x in my_dict:
    print(x)
# Output: 0, 1, 2, 3, 4

# 3e.
x: int = 0
while x < len(my_dict):
    print(x)
    x += 1
# Output: 0, 1, 2, 3, 4

# 3f.
x: int = 0
while x < len(my_dict):
    print(my_dict[x])
    x += 1
# Output: dog, cat, mouse, bird, whale

# 4
my_dict: dict[int, str] = {8: "dog", 1: "cat", 10: "mouse", 15: "bird", 0: "whale"}

# 4a.
for x in range(0, len(my_dict)):
    print(my_dict[x])
# Output: whale, cat, KeyError

# 4b.
for x in range(0, len(my_dict)):
    print(x)
# Output: 0, 1, 2, 3, 4

# 4c.
for x in my_dict:
    print(my_dict[x])
# Output: dog, cat, mouse, bird, whale

# 4d.
for x in my_dict:
    print(x)
# Output: 8, 1, 10, 15, 0

# 4e.
x: int = 0
while x < len(my_dict):
    print(x)
    x += 1
# Output: 0, 1, 2, 3, 4

# 4f.
x: int = 0
while x < len(my_dict):
    print(my_dict[x])
    x += 1
# Output: whale, cat, KeyError

# 5
my_dict: dict[str, str] = {
    "cat": "dog",
    "dog": "cat",
    "bird": "mouse",
    "mouse": "bird",
    "while": "whale",
}

# 5a.
for x in range(0, len(my_dict)):
    print(my_dict[x])

# Output: KeyError

# 5b.
for x in range(0, len(my_dict)):
    print(x)
# Output: 0, 1, 2, 3, 4

# 5c.
for x in my_dict:
    print(my_dict[x])
# Output: dog, cat, mouse, bird, whale

# 5d.
for x in my_dict:
    print(x)
# Output: cat, dog, bird, mouse, while

# 5e.
x: int = 0
while x < len(my_dict):
    print(x)
    x += 1
# Output: 0, 1, 2, 3, 4

# 5f.
x: int = 0
while x < len(my_dict):
    print(my_dict[x])
    x += 1
# Output: KeyError


# 6.
def quiz(lst: list[str]) -> list[int]:
    result: list[int] = []
    for x in range(0, len(lst)):
        result.append(len(lst[x]))
    return result


# 7.
def quiz(lst: list[str]) -> int:
    x: int = 0
    for y in lst:
        x += len(y)
    return x


# 8.
def quiz(lst: list[str]) -> None:
    for x in range(0, len(lst)):
        lst[x] += "!"


# 9.
def quiz(string: str) -> list[str]:
    result: list[str] = []
    for character in string:
        result.append(character)
    return result


# 10.
def quiz(num: int) -> list[int]:
    """Create a list of the size of the input integer and assign it to a global variable"""
    new_list: list[int] = []
    for x in range(0, num):
        new_list.append(x)
    return new_list


size_list: list[int] = quiz(5)


# 11.
def quiz(lst: list[float], num: int, fl: float) -> list[float]:
    """insert float into the list[float] at the index specified by the int passed to the function"""
    result: list[float] = []

    for x in range(0, len(lst)):
        if x == num:
            result.append(num)
        result.append(lst[x])

    # if index is at the end, append the new float after last element
    if num >= len(lst):
        result.append(num)


# 12.
def quiz(lst: list[int]) -> list[int]:
    """Return a new list with only the even numbers"""
    even_numbers: list[int] = []
    for x in range(0, len(lst)):
        if lst[x] % 2 == 0:
            even_numbers.append(lst[x])
    return even_numbers


# 13.
def quiz(lst: list[str]) -> list[str]:
    """Only return strings containing 'a'"""
    new_list: list[str] = []
    for x in range(0, len(lst)):
        if "a" in lst:
            new_list.append(x)
    return new_list


# 14.
def quiz(lst: list[int]) -> int:
    """return largest num from list of ints"""
    biggest_num: int = lst[0]
    for x in range(0, len(lst)):
        if lst[x] > biggest_num:
            biggest_num = lst[x]
    return biggest_num


# 15.
def quiz(string: str) -> dict[str, int]:
    """count the vowels"""
    vowel_count: dict[str, int] = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    for char in range(0, len(string)):
        if string[char] in vowel_count:
            vowel_count[string[char]] += 1
    return vowel_count


# 16.
def quiz(lst1: list[int], lst2: list[int]) -> list[int]:
    both: list[int] = []
    for x in range(0, len(lst1)):
        for y in range(0, len(lst2)):
            if lst1[x] == lst2[y]:
                both.append(lst1[x])
    return both


# 17.
def quiz(lst: list[float]) -> float:
    """return list average, ignore negative nums"""
    total: float = 0
    count: int = 0

    idx: int = 0
    while idx < len(lst):
        if lst[idx] >= 0:
            total += lst[idx]
            count += 1
        idx += 1
    if count > 0:
        return total / count
    return 0


# 18.
def quiz(lst: list[str]) -> list[str]:
    new_list: list[str] = []

    while len(new_list) < len(lst):
        max_index = 0
        for x in range(1, len(lst)):
            if len(lst[x]) > len(lst[max_index]):
                max_index = x
        new_list.append(lst[max_index])
        lst[max_index] = ""
    return new_list


# 19.
def quiz(lst: list[str]) -> dict[str, int]:
    empty_dict: dict[str, int] = {}
    for x in range(0, len(lst)):
        empty_dict[lst[x]] = len(lst[x])
    return empty_dict


# 20.
def quiz(string: str) -> dict[str, int]:
    empty_dict[str, int] = {}
    for char in range(0, len(string)):
        if string[char] in empty_dict:
            empty_dict[string[char]] += 1
        else:
            empty_dict[string[char]] = 1
    return empty_dict


# odd and even
def odd_and_even(lst: list[int]) -> list[int]:
    """odd and even function"""
    odd: list[int] = []
    idx: int = 0
    while idx < len(lst):
        if idx % 2 == 0 and lst[idx] % 2 == 1:
            odd.append(lst[idx])
        i += 1

    return odd


# short_words
def short_words(lst: list[str]) -> list[str]:
    """return words less than 5 chars"""
    short: list[str] = []
    idx: int = 0

    while idx < len(lst):
        if len(lst[idx]) > 5:
            print("The word is too long")
        else:
            short.append(lst[idx])
        idx += 1
    return short


# value_exists
def value_exists(dictionary: dict[str, int], num: int) -> bool:
    """does the value exist in the dictionary?"""
    for key in dictionary:
        if dictionary[key] == num:
            return True
    return False


# plus_or_minus_n
def plus_or_minus_n(inp: dict[str, int], n: int) -> None:
    for key in inp:
        if inp[key] % 2 == 0:
            inp[key] += n
        else:
            inp[key] -= n


# free_biscuits
def free_biscuits(games: dict[str, list[int]]) -> dict[str, bool]:
    """will UNC students win free biscuits (if bball team scores over 100 pts)?"""
    # check if the values in the dict add up to 100
    result: dict[str, bool] = {}
    for key in games:
        # sum up the values for each element of the dict
        list_to_sum: list[int] = games[key]
        sum: int = 0
        # loop thru list and add each value to sum
        for element in list_to_sum:
            sum += element
        # if sum >= 100, store in result under key "key" with value True
        if sum >= 100:
            result[key] = True
        else:
            result[key] = False
    return result


# Class writing
class Course:
    """Models the idea of a UNC course"""

    name: str
    level: int
    prerequisites: list[str]

    def find_courses(courses: list[Course], prereq: str) -> list[str]:
        """Finds 400 level courses with the given prereq"""
        results: list[str] = []

        for c in courses:
            if c.level >= 400:
                for p in c.prerequisites:
                    if p == prereq:
                        results.append(c.name)
        return results

    def is_valid_course(self, prereq: str) -> bool:
        """Whether course's level is 400+ and if its prerequisites list contains the given string"""
        if self.level < 400:
            return False
        for p in self.prerequisites:
            if p == prereq:
                return True
        return False


class HotCocoa:
    has_whip: bool
    flavor: str
    marshmallow_count: int
    sweetness: int

    def __init__(
        self, has_whip: bool, flavor: str, marshmallow_count: int, sweetness: int
    ):
        self.has_whip = has_whip
        self.flavor = flavor
        self.marshmallow_count = marshmallow_count
        self.sweetness = sweetness

    def mallow_adder(self, mallows: int) -> None:
        self.marshmallow_count += mallows
        self.sweetness += mallows * 2

    def __str__(self) -> str:
        if self.has_whip:
            return f"A {self.flavor} cocoa with whip, {self.marshmallow_count} marshmallows, and level {self.sweetness} sweetness."
        else:
            return f"A {self.flavor} cocoa without whip, {self.marshmallow_count} marshmallows, and level {self.sweetness} sweetness."


def order_cost(hotlist: list[HotCocoa]) -> float:
    cost: float = 0.0
    for x in hotlist:
        if x.has_whip:
            cost += 2.50
        else:
            cost += 2.0
    return hotlist


my_order: HotCocoa = HotCocoa(False, "chocolate", 5, 2)
my_order.has_whip = True
my_order.mallow_adder(2)
other_order: HotCocoa = HotCocoa(True, "peppermint", 10, 2)
order_cost([my_order, other_order])
print(my_order)
