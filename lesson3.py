# Functions

numbers = [12, 45, 7, 89, 23, 56]

print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])


def find_largest(numbers):
    largest = numbers[0]

    for i in numbers:
        if i > largest:
            largest = i
    return largest

result = find_largest(numbers)
print("Largest number is:", result)

#DSA problem 3

def find_even_numbers(numbers):
    count = 0
    for i in numbers:
        if i % 2 ==0:
            count +=1
    return count

result = find_even_numbers(numbers)
print("Number of even numbers is:", result)

#DSA problem 4

def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

result = calculate_average(numbers)
print("Average of numbers is:", result)