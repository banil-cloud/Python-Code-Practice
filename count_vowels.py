s = "Hello World"
vowels = 'aeiouAEIOU'
count = sum(1 for char in s if char in vowels)
print("Number of vowels:", count)
