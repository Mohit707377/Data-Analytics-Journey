# Day 04 — Python Loops & Problem Solving

## 1. Introduction to Loops

A loop is used to repeat something multiple times.

Loops are useful when we want to execute the same block of code repeatedly.

### Types of Loops

- For Loop
- While Loop
- While True
- Nested Loop


## 1.1 For Loop

A `for` loop is used to repeat a block of code for a given range.

The `range()` function is commonly used with a `for` loop.

### Syntax

for variable in range(start, stop):
    
    print(variable)
    
Example:

```python
for i in range(1, 6):
    print(i)
```
Output:

1
2
3
4
5

The ending value of range() is not included.

### Multiplication Table
```python
num = int(input("Enter the number: "))

for i in range(1, 11):

    print(num, "x", i, "=", num * i)
```
## 1.2 While Loop

A `while` loop executes a block of code as long as the given
condition is `True`.

In a `while` loop, the increment is usually done inside the loop.

Syntax:
while condition:
    # code
    increment
    
Example:
```python
n = 0
while n <= 10:
    print(n)
    n += 1
```
### Multiplication Table

```python
num = int(input("Enter the number: "))
n = 0
while n <= 10:
    print(num, "x", n, "=", num * n)
    n += 1
```
## 1.3 While True

`while True` creates an infinite loop because the condition
is always `True`.

To stop an infinite loop, the break statement is used.

Syntax:
while True:
    # code
    if condition:
        break
        
Example:
```python
while True:

    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    print(num1 + num2)

    choice = input("Do you want to stop? Say yes: ")

    if choice == "yes":
        break
```
## 1.4 Nested Loops

A `loop` inside another loop is called a `nested loop`.

Nested `loops` are also used to solve pattern problems.

Example:
```python
for i in range(1, 4):

    for j in range(1, 11):
        print(j)
```
The inner `loop` executes for each iteration of the outer `loop`.

# 2. Problem Solving

## Questions

1. Write a program to check whether a number is positive or not.

2. Write a program to check whether a number is even or odd.

3. Make an Area Calculator.

4. Write a program to check whether a letter is a vowel or not.

5. Write a program to check whether a number is single-digit,
   double-digit, or more than two-digit.
