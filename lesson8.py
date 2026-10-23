# 1. String operations
text = "  I am learning AI Engineering  "

print(text.lower())
print(text.upper())
print(text.strip())
print(text.replace("AI", "Machine Learning"))

# 2. Clean text for an AI application

user_input = "   MACHINE learning IS interesting   "

cleaned_text = user_input.strip().lower()

print(cleaned_text)

# 3. List comprehensions

numbers = [1, 2, 3, 4, 5]

squares = [number * number for number in numbers]

print(squares)

# With a condition

numbers = [12, 45, 7, 89, 23, 56]

even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers)

# 4. Dictionary comprehensions

num = [1,2,3,4,5]

squares = {number: number * number for number in num}
print(squares)

# 5. enumerate() — Get both index and value
# This is useful when processing rows, tokens, or items in a dataset.
words = ["AI", "Machine Learning", "Deep Learning"]

for index, word in enumerate(words):
    print(index, word)


# Challange 1

# Clean a line
text = "  Python is Fun  "
cleaned_text = text.strip().lower()
print(cleaned_text)

# Challenge 2
# Exttract long wods

words = ["AI", "Machine Learning", "Deep Learning", "Python", "Data Science"
""]

long_words = [word for word in words if len(word)>5]
print(long_words)

# Challenge 3
# Squre even numbers
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [number ** 2 for number in num if number % 2 == 0]
print(squares)

# Challenge 4
#Create a word-length dictionary

words = ["AI", "Machine Learning", "Deep Learning", "Python", "Data Science"]
word_length_dict = {word: len(word) for word in words}
print(word_length_dict)

#challenge 5
# Number the words using enumerate()

words = ["RAG", "LLM", "AI"]
for index, word in enumerate(words, start=1):
    print(index, word)