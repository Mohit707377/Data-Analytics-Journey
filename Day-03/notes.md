# Day 03 — Python Operators & Conditional Statements

## 1. Operators

Operators are special symbols or keywords used to perform operations on values or variables.

Operands are the values on which an operator performs an operation.

### Example

```python
a = 10
b = 5
c = a + b
print(c)
```
Here:

`+` is the operator.
a and b are operands.

## Types of Operators

## Python operators can be divided into different categories:

-Arithmetic Operators

-Comparison Operators

-Logical Operators

-Assignment Operators

-Identity Operators

-Bitwise Operators

-Membership Operators

## 1.1 Arithmetic Operators

Arithmetic operators are used to perform mathematical operations.

| Operator | Name | Example |
|----------|------|---------|
| `+` | Addition | `10 + 5 = 15` |
| `-` | Subtraction | `10 - 5 = 5` |
| `*` | Multiplication | `10 * 5 = 50` |
| `/` | Division | `10 / 5 = 2.0` |
| `%` | Modulus | `10 % 3 = 1` |
| `**` | Exponentiation | `2 ** 3 = 8` |
| `//` | Floor Division | `10 // 3 = 3` |


Example
``` python
a = 10
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print(a // b)
```
## 1.2 Comparison Operators

Comparison operators are used to compare two values.

They return either True or False.

| Operator | Meaning |
|----------|---------|
| `<` | Less than |
| `<=` | Less than or equal to |
| `>` | Greater than |
| `>=` | Greater than or equal to |
| `==` | Equal to |
| `!=` | Not equal to |

Example
``` python
a = 10
b = 5

print(a > b)
print(a < b)
print(a == b)
print(a != b)
```
## 1.3 Logical Operators

## 1.3 Logical Operators

Logical operators are used to combine or modify conditions.

### `and`

The `and` operator returns `True` only when both conditions are `True`.

**Example:**

```python
age = 22

print(age >= 18 and age <= 25)
```
Output:

True
### or

The `or` operator returns `True` when at least one condition is `True`.

Example:
```python
age = 22

print(age < 18 or age > 20)
```
Output:

True
### not

The `not` operator reverses the result of a condition.

Example:
```python
age = 22

print(not(age > 18))
```
Output:

False

## 1.4 Assignment Operators

Assignment operators are used to assign and update values in variables.

| Operator | Example | Equivalent |
|----------|---------|-------------|
| `=` | `x = 5` | `x = 5` |
| `+=` | `x += 5` | `x = x + 5` |
| `-=` | `x -= 5` | `x = x - 5` |
| `*=` | `x *= 5` | `x = x * 5` |
| `/=` | `x /= 5` | `x = x / 5` |
| `%=` | `x %= 5` | `x = x % 5` |
| `**=` | `x **= 5` | `x = x ** 5` |
| `//=` | `x //= 5` | `x = x // 5` |

Example
```python
x = 10
x += 5
`
print(x)
```

## 1.5 Identity Operators

Identity operators are used to check whether two variables refer to the same object.

### is

Returns `True` if both variables refer to the same object.

### is not

Returns `True` if both variables do not refer to the same object.

Example
``` python
a = [1, 2, 3]
b = a

print(a is b)
print(a is not b)
```
## 1.6 Bitwise Operators

Bitwise operators work with the binary representation of numbers.

| Operator | Name |
|----------|------|
| `&` | Bitwise AND |
| `|` | Bitwise OR |
| `^` | Bitwise XOR |
| `<<` | Left Shift |
| `>>` | Right Shift |

Example
```python
a = 5
b = 3

print(a & b)
print(a | b)
print(a ^ b)
print(a << 1)
print(a >> 1)
```
## 1.7 Membership Operators

Membership operators are used to check whether a value exists inside a sequence such as a string, list, or tuple.

### in

Returns ` True` if the value is present.

### not in

Returns `True` if the value is not present.

Example
```python
text = "hello"

print("h" in text)
print("z" not in text)
```
## 2. Conditional Statements

Conditional statements are used to make decisions in a program.

A block of code is executed when a given condition is true.

### 2.1 if Statement

The if statement executes a block of code when the condition is true.

Example
```python
marks = 95

if marks >= 90:
    print("Excellent")
```
### 2.2 if-else Statement

The if-else statement is used when there are two possible outcomes.

if executes when the condition is true.
else executes when the condition is false.
Example
```python
marks = 90

if marks >= 90:
    print("You get a job")
else:
    print("You need to work harder")
```
### 2.3 if-elif-else Statement

The if-elif-else statement is used when there are multiple conditions.

Python checks the conditions from top to bottom.

Example
```python
marks = 87

if marks >= 90:
    print("You will get a phone")
elif marks >= 70:
    print("You will get a new book")
else:
    print("You will not get anything")
```
### 2.4 Nested if Statement

A nested if statement means using one if statement inside another if statement.

Example
```python
marks = 96

if marks >= 80:
    print("You passed")

    if marks >= 90:
        print("You can get a new phone")
    else:
        print("You can get a new book")
```
### 2.5 Short-hand if Statement

A short-hand if statement is used when only one statement needs to be executed.

Example
```python
marks = 97

if marks >= 90: print("Good")
```
### 2.6 Short-hand if-else Statement

A short-hand if-else statement allows us to write the condition in a single line.

Example
```python
marks = 90

print("Good") if marks >= 90 else print("Needs improvement")
```
