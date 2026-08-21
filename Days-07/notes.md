# Day 07 — Python Pattern Problems & Strings

## 1. Pattern Problem Solving



### Number Pattern

```python
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()
```
```
Output:
1
12
123
1234
12345
```
### Repeated Number Pattern
```python
for i in range(1, 6):
    for j in range(i):
        print(i, end="")
    print()
```
```
Output:
1
22
333
4444
55555
```
### Reverse Number Pattern
```python
for i in range(1, 6):
    for j in range(6, i, -1):
        print(j - i, end="")
    print()
```
## Star Pattern
```python
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()
```
```
Output:
*
**
***
****
*****
```
### Reverse Star Pattern
```python
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
```
```
Output:
*****
****
***
**
*
```
### Multiplication Patterns
```python
for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end=" ")
    print()
```
## 2. String Manipulation
A string is a sequence of characters.
A string can contain letters, numbers, spaces and special characters.
Creating a String
a = "Hello World"
print(a)
String Indexing
Each character in a string has an index.
a = "Harry Potter and the Goblet of Fire"

print(a[0])
The first character has index 0.
String Length
The len() function is used to find the length of a string.
a = "Hello World"

print(len(a))
Count Characters
The count() method is used to find how many times a character or substring occurs.
a = "Hello World"

print(a.count("o"))
Convert to Uppercase
The upper() method converts all letters to uppercase.
a = "hello world"

print(a.upper())
Convert to Lowercase
The lower() method converts all letters to lowercase.
a = "HELLO WORLD"

print(a.lower())
Find Index of a Character
The index() method returns the index of a character or substring.
a = "Hello World"

print(a.index("o"))
Capitalize
The capitalize() method converts the first character of the string to uppercase.
a = "hello world"

print(a.capitalize())
Find a Character
The find() method returns the index of the first occurrence of a character or substring.
a = "Hello World"

print(a.find("o"))
String Formatting
The format() method is used to insert values into a string.
name = "John"

b = "My name is {}"

print(b.format(name))
Output:
My name is John
Center a String
The center() method places a string in the center of a given width.
name = "Mohit"

print(name.center(20))
3. String Functions
String functions can be used to check different properties of a string.
isalnum()
Returns True if all characters are alphanumeric.
a = "Hello123"

print(a.isalnum())
isalpha()
Returns True if all characters are alphabets.
a = "Hello"

print(a.isalpha())
isdecimal()
Returns True if all characters are decimal characters.
a = "1234"

print(a.isdecimal())
isdigit()
Returns True if all characters are digits.
a = "1234"

print(a.isdigit())
isnumeric()
Returns True if all characters are numeric.
a = "1234"

print(a.isnumeric())
islower()
Returns True if all cased characters are lowercase.
a = "hello"

print(a.islower())
isupper()
Returns True if all cased characters are uppercase.
a = "HELLO"

print(a.isupper())
isspace()
Returns True if all characters are whitespace characters.
a = "   "

print(a.isspace())
istitle()
Returns True if the string follows title-case rules.
a = "Hello World"

print(a.istitle())
4. Slicing in Strings
String slicing is used to get a part of a string.
Syntax
string[start:stop:step]
Example
a = "Harry Potter and the Goblet of Fire"

print(a)
print(a[0:5])
print(a[6:12])
print(a[-4:])
Slicing with Step
b = "0123456789"

print(b)
print(b[::3])
print(b[:7:2])
print(b[::2])
print(b[6::-1])
The step value determines how many positions are skipped while slicing.
5. Problem Solving
5.1 Separate String Values
The split() method can be used to separate a string into different values.
a = "OOTD.YOLO.ASAP.BRB.GTG.OTW"

b = a.split(".")

print(b)
5.2 Sort a String Alphabetically
The sorted() function can be used to sort characters alphabetically.
a = input("Enter anything: ")

b = sorted(a)

print(b)
5.3 Remove a Character from a String
The replace() method can be used to remove a character.
a = "hello"

b = a.replace("e", "")

print(b)
5.4 Remove Dots from a String
a = "F.R.I.E.N.D.S"

b = a.replace(".", "")

print(b)
5.5 Count Occurrences in a String
The count() method can be used to count the occurrence of a substring.
a = "she sells seashells on the sea shore"

b = a.count("sea")

print("The number of times 'sea' occurs is:", b)
5.6 Reverse a String
String slicing can be used to reverse a string.
a = input("Enter anything here: ")

b = a[::-1]

print(b)
5.7 Check if a String Contains Only Digits
The isdigit() method checks whether all characters in a string are digits.
a = input("Enter anything here: ")

print(a.isdigit())
5.8 Check Palindrome
A palindrome reads the same forward and backward.
a = input("Enter anything here: ")

rev = a[::-1]

if a == rev:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
5.9 Count Number of Vowels
A loop can be used to count vowels in a string.
a = input("Enter anything here: ")

vowels = 0

for i in a:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        vowels += 1

print("Number of vowels:", vowels)
5.10 Check Capitalization of Every Word
The istitle() method can be used to check whether every word follows title-case rules.
a = input("Enter anything here: ")

print(a.istitle())
