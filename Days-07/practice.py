# Day 07 - String Problem Solving


# 1. Separate values of a string

a = "OOTD.YOLO.ASAP.BRB.GTG.OTW"

b = a.split(".")

print("Separated values:", b)


# 2. Sort a string alphabetically

a = input("Enter a string: ")

b = sorted(a)

print("Sorted string:", b)


# 3. Remove a specific character from a string

a = input("Enter a string: ")
char = input("Enter the character to remove: ")

b = a.replace(char, "")

print("After removing character:", b)


# 4. Remove dots from a string

a = "F.R.I.E.N.D.S"

b = a.replace(".", "")

print("After removing dots:", b)


# 5. Count occurrence of a substring

a = "she sells seashells on the sea shore"

b = a.count("sea")

print("Number of occurrences:", b)


# 6. Reverse a string

a = input("Enter a string: ")

b = a[::-1]

print("Reversed string:", b)


# 7. Check whether a string contains only digits

a = input("Enter a string: ")

if a.isdigit():
    print("String contains only digits")
else:
    print("String does not contain only digits")


# 8. Check whether a string is a palindrome

a = input("Enter a string: ")

rev = a[::-1]

if a == rev:
    print("It is a palindrome")
else:
    print("It is not a palindrome")


# 9. Count the number of vowels

a = input("Enter a string: ")

vowels = 0

for i in a:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        vowels += 1

print("Number of vowels:", vowels)


# 10. Check whether every word starts with a capital letter

a = input("Enter a string: ")

if a.istitle():
    print("Every word starts with a capital letter")
else:
    print("Every word does not start with a capital letter")
