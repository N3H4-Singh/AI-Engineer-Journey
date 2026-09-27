# for loop
for i in range(5):
    print(i)



#List 
num = [10, 20, 30, 40,50]
print(num)

print(num[3])
print(num[0])

# 10 → index 0
# 20 → index 1
# 30 → index 2
# 40 → index 3
# 50 → index 4

num1 = [10, 20, 30, 40, 50]
for num1 in num1:
    print(num1)


#DsA problem 1
#Find the largest number
num = [10, 20, 30, 40, 50]
largest = num[0]
for i in num:
    if i > largest:
        largest = i
print("Largest number is:", largest)

#DsA problem 2
#Find the largest number
numbers = [12, 45, 7, 89, 23, 56]
smallest = numbers[0]
for i in numbers:
    if i < smallest:
        smallest = i
print("Smallest number is:", smallest)

#DsA problem 3
#Find the largest number
numbers = [12, 45, 7, 89, 23, 56]
count = 0
for i in numbers:
    if i%2==0:
        count +=1
print("Number of even numbers is:", count)

    
