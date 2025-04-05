## 💻 Python Basic Programs

<details>
  <summary><strong>1. Write a Python program to swap two numbers.</strong></summary>

a = 5 b = 10
Swapping using a temporary variable

temp = a a = b b = temp

print("a =", a) print("b =", b)


**Output:**

a = 10 b = 5


</details>

<br>

<details>
  <summary><strong>2. Check if a number is even or odd.</strong></summary>

num = int(input("Enter a number: "))

if num % 2 == 0: print("Even") else: print("Odd")


</details>

<br>

<details>
  <summary><strong>3. Find the factorial of a number using recursion.</strong></summary>

def factorial(n): if n == 0 or n == 1: return 1 return n * factorial(n - 1)

print(factorial(5)) # Output: 120


</details>

<br>

<details>
  <summary><strong>4. Print the Fibonacci sequence up to n terms.</strong></summary>

n = 10 a, b = 0, 1

for _ in range(n): print(a, end=' ') a, b = b, a + b


</details>

<br>

<details>
  <summary><strong>5. Check if a string is a palindrome.</strong></summary>

text = "madam"

if text == text[::-1]: print("Palindrome") else: print("Not a Palindrome")


</details>

<br>

<details>
  <summary><strong>6. Find the largest element in a list.</strong></summary>

numbers = [10, 20, 35, 4, 98] print("Largest number:", max(numbers))


</details>

<br>

<details>
  <summary><strong>7. Count the number of vowels in a string.</strong></summary>

s = "Hello World" vowels = 'aeiouAEIOU' count = sum(1 for char in s if char in vowels) print("Number of vowels:", count)


</details>
