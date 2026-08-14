# Day 05 - Python Problem Solving


# Question 1:
# Count occurrences of a specific element in a list.

numbers = [10, 20, 10, 30, 10, 40]
element = 10

count = 0

for num in numbers:
    if num == element:
        count += 1

print("Occurrences:", count)


# Question 2:
# Print elements from a list present at odd index positions.

numbers = [10, 20, 30, 40, 50, 60, 70]

for i in range(len(numbers)):
    if i % 2 != 0:
        print(numbers[i])


# Question 3:
# Reverse a string using a for loop.

text = "Python"
reverse = ""

for char in text:
    reverse = char + reverse

print("Reversed string:", reverse)


# Question 4:
# Count vowels and consonants in a sentence.

sentence = "Python is easy"

vowels = 0
consonants = 0

for char in sentence.lower():
    if char in "aeiou":
        vowels += 1
    elif char.isalpha():
        consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)


# Question 5:
# Count the total number of digits in a number.

num = 123456
count = 0

for digit in str(num):
    count += 1

print("Total digits:", count)


# Question 6:
# Print a right-angled triangle number pattern using a loop.

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# Question 7:
# Print the decreasing pattern.

for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()


# Question 8:
# Print Alphabet pyramid (A, BB, CCC) pattern.

for i in range(1, 6):
    letter = chr(64 + i)

    for j in range(i):
        print(letter, end="")

    print()


# Question 9:
# Print a hollow square pattern.

n = 5

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# Question 10:
# Print a pyramid pattern of stars.

n = 5

for i in range(1, n + 1):
    print(" " * (n - i), end="")

    for j in range(2 * i - 1):
        print("*", end="")

    print()
