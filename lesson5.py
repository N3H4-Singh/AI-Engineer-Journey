# Conditions + Loops

# 1. if / elif / else

age = int(input("Enter your age: "))
if age <= 18:
    print("You are a minor.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")


Marks = int(input("Enter your marks: "))
if Marks >= 90:
    print("You got an A grade.")
elif Marks >= 80:
    print("You got a B grade.")
else:
    print("You got a C grade.")         

# 2. Comparison operators
x = 5
y = 10
print(x == y)  # False    equal
print(x != y)  # True     not equal
print(x < y)   # True     less than
print(x > y)   # False    greater than
print(x <= y)  # True     less than or equal
print(x >= y)  # False    greater than or equal


# 3. for loop

num = [12, 34, 56, 78, 90]
for number in num:
    print(number) 


numbers = [12, 45, 7, 89, 23, 56]

# 4. if + for

for number in numbers:
    if number % 2 == 0:
        print(number)

# 5. range()

for i in range(5):
    print(i)