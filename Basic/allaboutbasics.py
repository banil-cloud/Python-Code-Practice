# Scenario-based Questions + Programs

"""Python data types:

str (strings)

int

float

bool

and basic operations (combining types, logical, comparison, etc.)"""

# Reverse a string.
s = "hello"
print(s[::-1])

# Check Palindrome
s = "madam"
print(s == s[::-1])

# Count vowels in string.
s = "programming"
vowels = "aeiou"
count = sum(1 for char in s if char in vowels)
print(count)

# Find the first non-repeating character
s = "aabbccde"
for c in s:
    if s.count(c) == 1:
        print(c)
        break

# Remove all spaces from a string
s = "Hello world"
print(s.replace(" ", ""))

# Replace all spaces with underscores
s = "this is python"
print(s.replace(" ", "_"))


# Replace vowels with '*'
s = "chatgpt"
vowels = "aeiou"
for v in vowels:
    s = s.replace(v, "*")
print(s)

# Check if two strings are anagrams.
s1 = "listen"
s2 = "silent"
print(sorted(s1) == sorted(s2))

# remove/Extract digits from a string.
s = "abc123def45"
digits = ''.join(filter(str.isdigit, s))
print(digits)

# Capitalize the first letter of each word
s = "hello world"
print(s.title())

# Find the most frequent character. 
from collections import Counter
s = "aabbbccdeee"
counter = Counter(s)
print(counter.most_common(1)[0][0])

# Find frequency of each character
s = "banana"
freq = {}
for char in s:
    freq[char] = freq.get(char, 0) + 1
print(freq)

# Find all substrings of length 3
s = "abcdef"
for i in range(len(s) -2):
    print(s[i:i+3])

# Check if string is anagram of another
a, b = "listen", "silent"
print(sorted(a) == sorted(b))

# Check if String contains only alphabets
s = "Python3"
print(s.isalpha())

# Integers
# Check if number is prime 
n = 7
print(all(n % i != 0 for i in range(2, int(n**0.5)+1)))
# print(all(n % i != 0 for i in range(2, int(n**0.5)+1)) and n > 1)

# Find factorial of a number
n = 5
fact = 1
for i in range(2, n+1):
    fact *= i
print(fact)

# Sum of digits of a number
n = 12345
print(sum(int(d) for d in str(n)))
# print(sum(map(int, str(n))))


# Reverse an integer
n = 1234
print(int(str(n)[::-1]))

# Check if number is Armstrong
n = 153
print(sum(int(d)**3 for d in str(n)) == n)

# digits = str(n)
# print(sum(int(d)**len(digits)) == n)


# Print all divisors of a number
n = 12
divisors = [i for i in range(1, n+1) if n % i == 0]

# Find GCD of two numbers
import math
print(math.gcd(54, 24))
#print(math.gcd(24, 36))

# Find LCM of two numbers.
import math
a, b = 12, 15
lcm = abs(a*b) // math.gcd(a, b)
print(lcm)

# Check if number is even or odd
n = 11
print("Even" if n % 2 == 0 else "Odd")

# Sum of first N natural numbers
N = 10
print(N*(N+1)//2)

# Find power without using ** operator
base, exp = 2, 5
result = 1
for _ in range(exp):
    result *= base
print(result)


# Count number of factors of a number
n = 12
factors = [i for i in range(1, n+1) if n % i == 0]
print(len(factors))


# Floats
# Round float to 2 decimal places
f = 3.14159
print(round(f, 2))

# Compare two floats safely
a, b = 0.1 + 0.2, 0.3
print(abs(a - b) < le-9)

# Add two floating point numbers.
a, b = 1.1, 2.2
print(a + b)

# Find square root
import math
f = 9.0
print(math.sqrt(f))

# Floor and ceiling of a float
import math
f = 5.7
print(math.floor(f), math.ceil(f))

# Convert string to float.
s = "3.14"
print(float(s))

# Convert float to integer
f = 12.99
print(int(f))

# Get fractional part of float.
f = 5.75
print(f - int(f))

# Check if a float is an integer.
f = 7.0
print(f.is_integer())

# Sum list of floats.
numbers = [1.1, 2.2, 3.3]
print(sum(numbers))

# Calculate area of a circle (float radius).
import math
r = 2.5
print(math.pi * r * r)

# Perform float diision.
print(5 /2)

# Format float with leading zeros
f = 3.5
print(f"{f:06.2f}")

# Generate randon float between two numbers.
import random
print(random.uniform(1.5, 3.5))

# Calculate BMI
weight = 70.0 # kg
height = 1.75 # meters
bmi = weight / (height ** 2)
print(round(bmi, 2))


# Format float with commas
f = 1234567.8912
print(f"{f:,.2f}")

#--------------------------------------------
#Booleans (bool)

# Check if list is empty
lst = []
print(bool(lst))

# Check if string is non-empty
s = "hello"
print(bool(s))

print(bool(""), bool("hello")) # Boolean from string

# Check if number is positive
n = -5
print(n > 0)

# Boolean conversion of None
print(bool(None))

# Use of or operator
a, b = False, False
print(a or b)

# Logical AND operatin
a, b = True, False
print(a and b)

# Logical NOT operation.
a = True
print(not a)

# Negate a boolean
flag = True
print(not flag)

# Multiple conditions check
age = 20
print(18 <= age <= 30)

# Boolean from integer zero
print(bool(0))
print(bool(0), bool(5)) # Boolean from integer

# Boolean from float non-zero
print(bool(0.01))

# Check if all elements are True
values = [True, True, False]
print(all(values))

# Check if any element is True
values = [False, False, True]
print(any(values))

# Use bool for conditions.
score = 85
passed = score >= 50
print(passed)

#----------------------------------------------------

# Basic Operations

# Addition of two numbers.
a, b = 3, 5
print(a + b)

# Concatenate int to string
age = 25
print("Age is" + str(age))

# Multiply string with int
print("Hi" * 3)

# Compare int and float
print(5 == 5.0)

# Subtraction of two numbers
a, b = 4, 6
print(a * b)

# Division of two numbers.
a, b = 8, 2
print(a / b)

# Floor division
a, b = 7, 3
print(a // b)

# Modules operation.
a, b = 7, 3
print(a % b)

# Exponentiation operation
a, b = 2, 3
print(a ** b)

# Find maximum of two numbers.
a, b = 4, 10
print(max(a, b))

# Find minimum of two numbers.
a, b = 4, 10
print(min(a, b))

# Swapping two variables. 
a, b = 5, 10
a, b = b, a
print(a, b)

# Check type after addition
result = 1 + 2.0
print(type(result))

# Comparision chain
x = 5
print(1 < x < 10)
