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
```
Output:
54321
4321
321
21
1
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
for i in range(1, 11):
    for j in range(1, i+1):
        print(i * j, end=" ")
    print()
```
```
Output:
1
2 4
3 6 9
4 8 12 16
5 10 15 20 25
6 12 18 24 30 36
7 14 21 28 35 42 49
8 16 24 32 40 48 56 64
9 18 27 36 45 54 63 72 81
10 20 30 40 50 60 70 80 90 100
```
## 2. String Manipulation
A string is a sequence of characters.
A string can contain letters, numbers, spaces and special characters.
### Creating a String
```puthon
a = "Hello World"
print(a)
```
### String Indexing
Each character in a string has an index.
```python
a = "Harry Potter and the Goblet of Fire"
print(a[0])
#The first character has index 0.
```
### String Length
The len() function is used to find the length of a string.
```python
a = "Hello World"
print(len(a))
```
### Count Characters
The count() method is used to find how many times a character or substring occurs.
```python
a = "Hello World"
print(a.count("o"))
```
### Convert to Uppercase
The upper() method converts all letters to uppercase.
```python
a = "hello world"
print(a.upper())
```
### Convert to Lowercase
The lower() method converts all letters to lowercase.
```python
a = "HELLO WORLD"
print(a.lower())
```
### Find Index of a Character
The index() method returns the index of a character or substring.
```python
a = "Hello World"
print(a.index("o"))
```
### Capitalize
The capitalize() method converts the first character of the string to uppercase.
```python
a = "hello world"
print(a.capitalize())
```
### Find a Character
The find() method returns the index of the first occurrence of a character or substring.
```python
a = "Hello World"
print(a.find("o"))
```
### String Formatting
The format() method is used to insert values into a string.
```python
name = "John"
b = "My name is {}"
print(b.format(name))
```
```
Output:
My name is John
```
### Center a String
The center() method places a string in the center of a given width.
```python
name = "Mohit"
print(name.center(20))
```
## 3. String Functions
String functions can be used to check different properties of a string.
### isalnum()
Returns True if all characters are alphanumeric.
```python
a = "Hello123"
print(a.isalnum())
```
### isalpha()
Returns True if all characters are alphabets.
```python
a = "Hello"
print(a.isalpha())
```
### isdecimal()
Returns True if all characters are decimal characters.
```python
a = "1234"
print(a.isdecimal())
```
### isdigit()
Returns True if all characters are digits.
```python
a = "1234"
print(a.isdigit())
```
### isnumeric()
Returns True if all characters are numeric.
```python
a = "1234"
print(a.isnumeric())
```
### islower()
Returns True if all cased characters are lowercase.
```python
a = "hello"
print(a.islower())
```
### isupper()
Returns True if all cased characters are uppercase.
```python
a = "HELLO"
print(a.isupper())
```
### isspace()
Returns True if all characters are whitespace characters.
```python
a = "   "
print(a.isspace())
```
### istitle()
Returns True if the string follows title-case rules.
```python
a = "Hello World"
print(a.istitle())
```
## 4. Slicing in Strings
String slicing is used to get a part of a string.
```Syntax:
string[start:stop:step]
```
Example:
```python
a = "Harry Potter and the Goblet of Fire"

print(a)
print(a[0:5])
print(a[6:12])
print(a[-4:])

#Slicing with Step
b = "0123456789"

print(b)
print(b[::3])
print(b[:7:2])
print(b[::2])
print(b[6::-1])
```
The step value determines how many positions are skipped while slicing.
## String Problem Solving — 10 Questions

1. Write a program to separate the values of a string using `split()`.

2. Write a program to sort the characters of a string alphabetically.

3. Write a program to remove a specific character from a string.

4. Write a program to remove dots (`.`) from a string.

5. Write a program to count the occurrence of a specific substring in a string.

6. Write a program to reverse a string.

7. Write a program to check whether a string contains only digits.

8. Write a program to check whether a string is a palindrome.

9. Write a program to count the number of vowels in a string.

10. Write a program to check whether every word in a string starts with a capital letter.
