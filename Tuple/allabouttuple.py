""" A tuple in python is a n immutable , ordered collection of elements. Unlike list,
tuples cannot be modified after creation. they are defined using parentheses ()."""

# Basic functionality
my_tuple = (10, 20, 30)
print(my_tuple)
print(my_tuple[0]) # Accessing element.

# Find sum of all elements in Tuple
nums = (1, 2, 3, 4)
print(sum(nums))

# print all items in Uppercase in tuple
words = ("hello", "world")
upper_words = tuple(word.upper() for word in words)
print(upper_words)

# Mixed type tuple
mixed = (1, "apple", 3.14, True)
print(mixed)

# Nested Tuple
nested = ((1, 2), (3, 4))
print(nested[0][1]) # Output : 2

# Tuple of Dictionaries
tpl_dicts = ({"a": 1}, {"b": 2})
print(tpl_dicts[1]["b"]) # Output : 2

# Tuple with Duplicate Values
tpl = (1, 2, 2, 3, 3, 3)
print(tpl.count(3))  # Output: 3

# Tuple of list
tpl_lists = ([1, 2], [3, 4])
tpl_lists[0].append(5)
print(tpl_lists) # Output: ([1, 2, 5], [3, 4])

# Empty Tuple
empty = ()
print(empty)

# Tuple with Boolean Values
tpl_bool = (True, False, True)
print(all(tpl_bool)) # Output : False

# Tuple of Tuple with Uneven lengths.
tpl = ((1,), (2, 3), (4, 5, 6))
print(tpl[2][1])  # Output : 5

# Tuple of Ranges
tpl_ranges = (range(5), range(1, 4))
for r in tpl_ranges:
    print(list(r))  # Output: [0, 1, 2, 3, 4] then [1, 2, 3]

# Tuple of File Names
files = ("file1.txt", "image.png", "doc.pdf")
print(files)

# Tuple with None Values. 
tpl_none = (None, 1, None, 3)
print(tpl_none.count(None))  # Output: 2

# Tuple of Boolean to Decision
tpl = (True, False)
decisions = ("Proceed", "Stop")
for i in tpl:
    print(decisions[i == False]) # Output: Stop, Proceed

# Tuple of Characters
chars = tuple("hello")
print(chars)  #Output: ('h', 'e', 'l', 'l', 'o')

# Tuple of Even Numbers from 1 to 20
evens = tuple(i for i in range(1, 21) if i % 2 == 0)
print(evens)

# Tuple in Reverse Oder
tpl = (1, 2, 3, 4)
print(tpl[::-1]) # Ouput: (4, 3, 2, 1)

# Tuple with Repeated patterns
pattern = ("A", "B") * 3
print(pattern) #Output: ('A', 'B', 'A', 'B', 'A', 'B')

# Tuple from user input
user_input = input("Enter comma-separated values: ") # eg 1, 2, 3
tpl = tuple(user_input.split(","))
print(tpl)

# Tuple Slicing
tpl = (1, 2, 3, 4, 5)
print(tpl[1:4])

# Adding Elements (Tuple are immutable - use concatenation)
tpl = (1, 2)
tpl = tpl + (3, )
print(tpl) # Output: (1, 2, 3)

# Remove elements (Not directly possible; convert to list)
tpl = (1, 2, 3)
tpl = tuple(x for x in tpl if x != 2)
print(tpl)

# Insert() Add (only with conversion)
tpl = (1, 3)
lst = list(tpl)
lst.insert(1, 2)
tpl = tuple(lst)
print(tpl) # Ouput : (1, 2, 3)

# Add multiple items at the end (tuples are immutable, so convert to list)
tpl = ("apple", "banana", "cherry")
tpl_extended = tuple(list(tpl) + ['orange', 'grape'])
print("Extended:", tpl_extended)


# Remove item at specific index
tpl_list = list(tpl)
tpl_list.pop(1)
tpl_removed = tuple(tpl_list)
print("After pop:", tpl_removed)


# Delete by index or whole tuple
tpl_temp = list(tpl)
del tpl_temp[0]  # delete by index
print("After deleting index 0:", tuple(tpl_temp))


# del tpl # deletes entire tuple object
# clear all items
tpl_clear = ()
print("Cleared tuple:", tpl_clear)

# Make one item capitalize (change one item)
tpl_cap = tuple(word.upper() if word == 'banana' else word for word in tpl)
print("One capitalized:", tpl_cap)


# Capitalize all items
tpl_all_cap = tuple(word.upper() for word in tpl)
print("All capitalized:", tpl_all_cap)

# Capitalize repeated items (e.g., all 'apple')
tpl_repeated = ('apple', 'banana', 'apple', 'cherry')
tpl_mod = tuple(w.upper() if w == 'apple' else w for w in tpl_repeated)
print("Repeated capitalized:", tpl_mod)


# Make every word title case
tpl_title = tuple(word.title() for word in tpl)
print("Title case:", tpl_title)

# Sort tuple (convert to list to sort)
tpl_sort = tuple(sorted(tpl))
print("Sorted:", tpl_sort)

# Reverse tuple
tpl_rev = tpl[::-1]
print("Reversed:", tpl_rev)


# Count(), index()
print("Count 'apple':", tpl.count('apple'))
print("Index of 'banana':", tpl.index('banana'))


# Copy (Tuples are immutable, but shallow copy)
tpl_copy = tpl[:]
print("Copy:", tpl_copy)


# Operators (+, *)
print("Concatenated:", tpl + ('kiwi',))
print("Repeated:", tpl * 2)


# Slicing
print("Slice:", tpl[1:3])

# Zip(), map(), filter()
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
zipped = tuple(zip(tuple1, tuple2))
print("Zipped:", zipped)


# map() to double numbers
nums = (1, 2, 3)
mapped = tuple(map(lambda x: x * 2, nums))
print("Mapped (x2):", mapped)


# filter() to keep even
filtered = tuple(filter(lambda x: x % 2 == 0, nums))
print("Filtered (even):", filtered)


# Convert tuple to list
tpl_to_list = list(tpl)
print("To list:", tpl_to_list)

# Convert tuple to dict (only works if format is pair tuples)
tpl_dict = (('a', 1), ('b', 2))
dict_from_tuple = dict(tpl_dict)
print("To dict:", dict_from_tuple)

# Convert tuple to set
tpl_set = set(tpl)
print("To set:", tpl_set)

# Convert  back to tuple
print("Back to tuple from list:", tuple(tpl_to_list))
print("Back to tuple from set:", tuple(tpl_set))

