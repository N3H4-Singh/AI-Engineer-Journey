# While Loops, Break, Continue & Nested Loops

# 1. The while loop : A while loop repeats code as long as a condition is true.
count = 1

while count <=5:
    print(count)
    count += 1


#break — Stop the loop. break immediately exits the loop.

numbers = [12, 45, 7, 89, 23, 56]

for number in numbers:
    if number == 89:
        break
    print(number)

# 3. continue — Skip the current iteration and moves to the next one.

numbers = [12, 45, 7, 89, 23, 56]

for number in numbers:
    if number < 20:
        continue
    print(number)

# 4. Nested loops : is a loop inside another loop.

for i in range(1,4):
    for j in range(1,3):
        print(i,j)



# Challenge 1 - Countdown
# Use a while loop to print numbers from 10 down to 1, then print Start!
count = 10
while count <= 10 and count > 0:
    print (count)
    count -= 1
print("Start!")

# Challenge 2 — Sum of numbers
# Use a while loop to calculate the sum of numbers from 1 to 100. Expected result: 5050.

count = 1
sum = 0
while count <= 100:
    sum += count 
    count += 1
print(sum)

# Challenge 3 — Stop at a target
# Loop through [12, 45, 7, 89, 23, 56]. Print each number and stop when you reach 23. Should 23 be printed? Decide based on where you put break.
 
numbers = [12, 45, 7, 89, 23, 56]
for number in numbers:
    if number == 23:
        break
    print(number)
# Challenge 4 — Skip multiples
# Use continue to print numbers from 1 to 20, skipping multiples of 3.
for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i)

# Challenge 5 — Multiplication table
# Use nested loops to print multiplication tables for 2 and 3, from ×1 to ×5. ans of this
for i in range (2, 4):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}")
