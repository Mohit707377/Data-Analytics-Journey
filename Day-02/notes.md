# Day 02 — User Input, Type Casting & Problem Solving 🐍

## 1. User Input
The `input()` function is used to take input from the user.
By default, the `input()` function returns the input as a string.

### String Input
```python
name = input("Enter your name: ")
print(name)
```
Example Output

Enter your name: Mohit

Mohit

## 2. Integer Input
To take an integer input from the user, we use int() with input().
```python
age = int(input("Enter your age: "))
print(age)
```
Example Output

Enter your age: 22

22

## 3. Float Input
To take a decimal number as input, we use float() with input().
```python
age = float(input("Enter your age: "))
print(age)
```
Example Output

Enter your age: 22.5

22.5

## 4. eval()
The eval() function evaluates a string as a Python expression.
Example:
```python
result = eval(input("Enter any equation: "))
print(result)
```
If the user enters:

10 + 20

Output:

30

eval() should be used carefully with unknown or untrusted input.

## Type Casting and Type Conversion

Type casting means converting a value from one data type into another data type.
There are two main types of type conversion:
1.Implicit Type Conversion
2.Explicit Type Conversion

## 1. Implicit Type Conversion

Implicit type conversion happens automatically when Python converts one data type into another compatible data type.

Example:
```python
a = 24
b = 1.5
c = a + b
print(c)
print(type(c))
```
Output:

25.5

<class 'float'>

Here, Python automatically converts the integer value into a float during the calculation.

## 2. Explicit Type Conversion
Explicit type conversion happens when the programmer manually converts one data type into another.
Common type conversion functions are:
int()
float()
str()
bool()

Example:
```python
a = "123"
print(type(a))
a = int(a)
print("After conversion:", a)
print(type(a))
```
Output:

<class 'str'>

After conversion: 123

<class 'int'>

Here, the string "123" is explicitly converted into an integer using int().
