# Simple Integer List

# Find the sum of all elements in the list.
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print("Sum:", total)

# String List
# Print all items in uppercase
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit.upper())

# Mixed Type List
# Count how many items are integers.
mixed = [1, "two", 3.0, True]
count = sum(1 for item in mixed if isinstance(item, int))
print("Integer count:", count)

# Nested List
# Flatten the list into a single list.
nested = [[1, 2], [3, 4], [5, 6]]
flat = [item for sublist in nested for item in sublist]
print("Flattened List:", flat)

# List of Dictionaries
# Print names of people older than 26
people = [{"name": "Alice", "age": 25}, {"name": "bob", "age": 30}]
for person in people:
    if person["age"] > 26:
        print(person["name"])

# List with Duplicate Values
# Remove duplicates and sort the list
nums = [1, 2, 2, 3, 4, 4, 5]
unique_sorted = sorted(set(nums))
print("Unique sorted:", unique_sorted)


# List of tuple
# Print the second value of each tuple.
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
for _, value in pairs:
    print(value)

# Empty List
# Add numbers 1 to 5 using loop.
empty_list = []
for i in range(1, 6):
    empty_list.append(i)
print(empty_list)

# List with Boolean Values
bools = [True, False, True, True]
count_true = bools.count(True)
print("Number of True values:", count_true)

# List of lists with Uneven Lengths
uneven_lists = [[1], [2, 3], [4, 5, 6]]
for sublist in uneven_lists:
    print("Length:", len(sublist))


# Convert to a single list of numbers.
ranges = [range(1, 4), range(5, 7)]
flattened = [num for r in ranges for num in r]
print(flattened)

# List of File Names (string)
files = ["data1.csv", "data2.csv", "notes.txt"]
csv_files = [f for f in files if f.endswith(".csv")]
print(csv_files)

# Remove all None values
data = [1, None, 2, None, 3]
cleaned = [x for x in data if x is not None]
print(cleaned)

# List of Booleans to Decision
checks = [True, True, False]
result = "Pass" if all(checks) else "Fail"
print(result)


# Join them to form a string. 
chars = ['a', 'b', 'c', 'd']
joined = ''.join(chars)
print(joined)

# Create list of even number from 1 to 20
evens = [x for x in range(1, 21) if x % 2 == 0]
print(evens)


# Reverse the list without using [::-1]
nums = [10, 20, 30, 40]
nums.reverse()
print(nums)

names = ["apple", "banana", "cherry"]
names.reverse()
print(names)

# Repeat [1, 2] five times.
pattern = [1, 2] * 5
print(pattern)


# Ask for 5 numbers from user and store in a list
user_nums = []
for _ in range(5):
    user_nums.append(int(input("Enter a number: ")))
print("You entered: ", user_nums)

# List slicing (get only the middle 3 items)
nums = [10, 20, 30, 40, 50]
middle = nums[1:4]
print("Middle items: ", middle)

#add one item to the end of the list
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)

# insert() add one item at a specific position. 
fruits = ["apple", "Banana"]
fruits.insert(1, "orange") # Insert at index 1
print(fruits)

#extend() Add multiple items at end 
fruits = ["apple", "banana"]
fruits.extend(["cherry", "mango"])
print(fruits)

# remove() Remove first occurrence of an item.
fruits = ["apple", "banana", "cherry", "banana"]
fruits.remove("banana")
print(fruits)  # output: ['apple', 'cherry', 'banana']
# only first matching item is removed. 

# pop() Remove item at a specific index (or last item if no index given)
fruits = ["apple", "banana", "cherry"]
fruits.pop(1)  # Removes 'banana'
print(fruits)

fruits.pop()
print(fruits)


# del - Delete by index or whole list
fruits = ["apple", "banana", "cherry"]
del fruits[0]   # Delete item at index 0
print(fruits)   # Output: ['banana', 'cherry']

del fruits() # delete the entire list

# Clear() - Remove all items (empty the list)
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)

# print specific item in capitals
fruits = ["apple", "banana", "cherry"]
index = fruits.index("banana")  # Find the index of "banana"
fruits[index] = fruits[index].upper()  # Replace 'banana' with its uppercase version
print(fruits)   # ['apple', 'BANANA', 'cherry']

# index() finds where "banana" is in the list. 

# if banana repeats in list and make all capital

fruits = ["apple", "banana", "cherry", "banana"]
fruits = [fruit.upper() if fruit == "banana" else fruit for fruit in fruits]  # Convert all banana to BANANA
print(fruits)


# Make the first letter of every word capital. 
# using .capitalize()
fruits = ["apple", "banana", "cherry", "mango"]
capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print(capitalized_fruits)

title_fruits = [fruit.title() for fruit in fruits]
print(title_fruits)

# capitalize() only first becomes capital like apple banana becomes Apple banana
# title() every word becomes capital apple banana becomes Apple Banana

nums = [4, 1, 5, 2]
nums.sort()
print(nums)  # Output : [1, 2, 4, 5]

nums = [4, 1, 5, 2]
new_nums = sorted(nums)
print(new_nums)  # Output : [1, 2, 4, 5]


# Copy a list without affecting original
a = [1, 2, 3]
b = a.copy()
b.append(4)
print(a)  # Output : [1, 2, 3]
print(b)  # Output : [1, 2, 3, 4]


# Count how many times a specific item appear. 
nums = [1, 2, 2, 3, 2]
print(nums.count(2)) # Output : 3

# Find index where item is found first. 
fruits = ["apple", "banana", "cherry"]
print(fruits.index("banana"))  # Output : 1

# * operator (repeat list)
lst = [1, 2]
print(lst * 3) # OUtput : [1, 2, 1, 2, 1, 2]

# Combine two lists
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 95]
combined = list(zip(names, scores))  # Combine them using zip
print(combined)

# Filter only keep items that match the condition (x % 2 == 0 means even numbers)
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers)) # keep only even numbers
print(evens)

# Convert list to Dict
list1 = ["a", 1, "b", 2]
dict1 = dict(zip(list1[::2],list1[1::2]))
print(dict1)  # {'a': 1, 'b': 2}

# list[::2] Picks elements at even indexes ('a', 'b')
# list[1::2] Picks elements at odd indexes (1, 2)

# convert list to tuple
list1 = [1, 2, 3]
tuple1 = tuple(list1)  # Convert list to tuple
print(tuple1)

# convert list to set
list1 = [1, 2, 2, 3]
set1 = set(list1) # convert list to set and removes duplicates.
print(set1)

