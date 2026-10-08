#Dictionaries + Tuples + Sets

#A dictionary stores data as key → value pairs.
student = {
    "name": "Neha",
    "age": 22,
    "cgpa": 8.5,
    "branch": "CSE"
}
print(student)

student["City"] = "Mumbai"

student["cgpa"] = 8.7

print(student)

for key, value in student.items():
    print(key, ":", value)

#List   → mutable
#Tuple  → immutable

# A tuple is similar to a list, but immutable.(doesn't change)

# Sets

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

categories = ["cat", "dog", "cat", "bird", "dog", "cat"]

unique_categories = set(categories)

print(unique_categories)


# Lesson 4 - Dictionaries, Tuples and Sets

student = {
    "name": "Neha",
    "age": 21,
    "skills": ["Python", "SQL", "Machine Learning"],
    "cgpa": 8.5
}

# Challenge 1
print(student["name"])

# Challenge 2
print(student["skills"][1])

# Challenge 3
student["target"] = "AI Engineer"
print(student)

# Challenge 4
languages = ["Python", "SQL", "Python", "Java", "SQL", "Python"]
unique_languages = set(languages)
print(unique_languages)

# Challenge 5
coordinates = (19.07, 72.87)

print(coordinates[0])
print(coordinates[1])

