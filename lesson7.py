# 1. What is a function?
# A function is a reusable block of code that performs a specific task.

def greet():
    print("Welcome to AI Engineer Journey!")
greet()

# 2. Functions with parameters
# Parameters let you pass information into a function.
def greet (name):
    print("Hello", name)

greet ("Alice")  
greet ("Bob")


#3. The return statement
# The return statement sends a result back to the code that called the function.
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(result)

# Challenge 1 — Create a square function
def square (num):
    return num * num
result = square(5)
print(result)

# Challenge 2 — Find the largest number without max()
def find_largest(numbers):
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    return largest

numbers = [12, 45, 7, 89, 23]
print(find_largest(numbers))

# Challenge 3 — Calculate the average
def calculate_average(numbers):
    if len(numbers) == 0:
        return 0

    total = 0

    for number in numbers:
        total += number

    return total / len(numbers)

numbers = [10, 20, 30, 40]
print(calculate_average(numbers))

# hallenge 4 — Classify confidence scores

def classify_confidence(score):
    if score < 0 or score > 1:
        return "Invalid"
    elif score >= 0.90:
        return "High"
    elif score >= 0.70:
        return "Medium"
    else:
        return "Low"


print(classify_confidence(0.95))
print(classify_confidence(0.72))
print(classify_confidence(0.50))
print(classify_confidence(1.5))

# Challenge 5 — Count high-confidence scores


def classify_confidence(score):
    if score < 0 or score > 1:
        return "Invalid"
    elif score >= 0.90:
        return "High"
    elif score >= 0.70:
        return "Medium"
    else:
        return "Low"


def count_high_scores(scores):
    count = 0

    for score in scores:
        if classify_confidence(score) == "High":
            count += 1

    return count


scores = [0.95, 0.72, 0.99, 0.61, 0.91]

print("High-confidence scores:", count_high_scores(scores))











