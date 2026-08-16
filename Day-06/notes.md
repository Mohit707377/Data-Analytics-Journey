# Day 06 — Python Loops & String Problem Solving

## 1. For Loop with Conditional Statements

A `for` loop can be used with conditional statements to check
conditions during each iteration.

Conditional statements such as `if`, `elif`, and `else` can
be used inside a `for` loop.
### Example

```python
for i in range(1, 101):
    if i == 3:
        print("Add this to the task")
    else:
        print(i)
```

## 2. Break Statement

The `break` statement is used to stop a loop immediately when
a particular condition is satisfied.

It terminates the loop and moves the program execution outside
the loop.
### Example

```python
for i in range(1, 11):
    if i == 5:
        break
    print(i)
```
## 3. Continue Statement

The `continue` statement is used to skip the current iteration
of a loop.

After using `continue`, the loop moves to the next iteration.
### Example

```python
for i in range(1, 11):
    if i == 5:
        continue
    print(i)
```

# 4. Loop Problem Solving

Loop-based problems can be solved by using `for` and `while`
loops along with conditional statements.

### Problems Practiced

- Sum of even numbers up to 50
- Square of first 20 numbers
- Sum of first 10 odd numbers using `while` loop
- Billing system

---

# 5. String Problem Solving

String problems can be solved using built-in string functions
and methods provided by Python.

### Problems Practiced

- Find the length of a string
- Count the occurrence of a character
- Convert string into lowercase
- Convert string into uppercase
- Convert string into title case
- Find the index of a substring

### Useful String Methods

- `len()` — Finds the length of a string
- `count()` — Counts the occurrence of a character or substring
- `lower()` — Converts a string into lowercase
- `upper()` — Converts a string into uppercase
- `title()` — Converts a string into title case
- `find()` — Finds the index position of a substring
