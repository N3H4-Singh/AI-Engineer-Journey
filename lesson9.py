# Day 9 — Python Modules, Exception Handling & File Handling

# 1. Python modules — Reusing code
# A module is a Python file containing code that you can import and reuse.
import math 

print (math.sqrt(25))
print(math.pi)
print(math.ceil(4.2))

# 2. Create your own module
# making my own function

def my_function(score):
    if score < 0 or score> 1:
        return "Invalid score"
    elif score>=0.90:
        return"A"
    elif score>=0.80:  
        return"B"
    elif score>=0.70:
        return"C"
    else:
        return"F"

from lesson9 import my_function
print(my_function(0.60))
print(my_function(0.80))
print(my_function(0.90))

# 3. Exception handling — try and except
try:
    num1 = int(input("Enter a number: "))
    print(num1)
except ValueError:
    print("Invalid input. Please enter a valid number.")


try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print("Division successful. Result:", result)
finally:
    print("Execution completed.")


# 4. File handling — Reading and writing data
with open("ai_notes.txt", "w", encoding="utf-8") as file:
    file.write("I am learning AI Engineering.\n")
    file.write("Next, I will learn NumPy and Pandas.")

print("File saved successfully.")


with open("ai_notes.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)

# 5. AI-oriented example — Validate and save prediction score

scores = [0.95, 0.72, -0.1, 0.88, 1.2, 0.97]

def classify_confidence(score):
    if score < 0 or score > 1:
        return "Invalid"
    elif score >= 0.90:
        return "High"
    elif score >= 0.70:
        return "Medium"
    else:
        return "Low"

with open("prediction_results.txt", "w", encoding="utf-8") as file:
    for score in scores:
        try:
            if not isinstance(score, (int, float)):
                raise TypeError("Score must be numeric")

            label = classify_confidence(score)
            result = f"Score: {score}, Classification: {label}"

            print(result)
            file.write(result + "\n")

        except TypeError as error:
            print("Error:", error)

print("Results saved to prediction_results.txt")