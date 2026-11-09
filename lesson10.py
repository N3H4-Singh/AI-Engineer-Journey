# Day 10 — Complete Python Revision (Lessons 1–9)


# Lesson 1: Variables and data types
name = "Neha"
age = 22
cgpa = 8.7
is_learning_ai = True

print( type(name))  
print( type(age))
print( type(cgpa))      
print( type(is_learning_ai))

# Lesson 2: Operators and basic calculations

a = 20
b = 5
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

age = 22
has_degree = True

print(age >= 18 and has_degree)

# Lesson 3: Lists and functions

num = [12, 54, 23, 67, 89]
print(num)
print(num[3])
print(max(num))
print(min(num))
print(len(num))
print(sum(num))

def find_largest(numbers):
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest
print(find_largest(num))

# Lesson 4: Dictionaries, tuples and sets
student = {
    "name": "Neha",
    "age": 22,
    "cgpa": 8.7
}

# Tuple
coordinates = (19.07, 72.87)
print(coordinates[0])

# Set
languages = {"Python", "SQL", "Python"}
print(languages)

# Lesson 5: Conditions and loops
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
else:
    print("Grade: C")

# for loop
for number in range(1,6):
    print(number)  


# Lesson 6: While loops, break and continue

count = 1
while count <= 5:
    print(count)
    count += 1

for number in range (1,11):
    if number == 5:
        continue
    print(number)


# Lesson 7: Functions, parameters, return and scope

def calculate_average(numbers):
    if not numbers:
        return 0

    return sum(numbers) / len(numbers)

scores = [80, 90, 70]

print(calculate_average(scores))

# Lesson 8: Strings and comprehensions

text = "  MACHINE LEARNING  "

print(text.strip().lower())

# list comprehension:

numbers = [1, 2, 3, 4, 5, 6]

squares = [n ** 2 for n in numbers if n % 2 == 0]

print(squares)

# Dictionary comprehension:
words = ["Python", "AI", "Data"]

lengths = {word: len(word) for word in words}

print(lengths)

# enumerate():
for index, word in enumerate(words, start=1):
    print(index, word)

# Lesson 9: Modules, exceptions and file handling

import math

print(math.sqrt(144))

try:
    number = int("hello")
except ValueError:
    print("Please enter a valid number")

# Writing and reading files:

with open("notes.txt", "w") as file:
    file.write("Learning Python for AI")

with open("notes.txt", "r") as file:
    print(file.read())