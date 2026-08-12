# Day 03 - Python Operators & Conditional Statements


# ==============================
# 1. Arithmetic Operators
# ==============================

a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
print("Floor Division:", a // b)


# ==============================
# 2. Comparison Operators
# ==============================

x = 10
y = 5

print(x < y)
print(x <= y)
print(x > y)
print(x >= y)
print(x == y)
print(x != y)


# ==============================
# 3. Logical Operators
# ==============================

age = 22

print(age >= 18 and age <= 25)
print(age < 18 or age > 20)
print(not(age > 18))


# ==============================
# 4. Assignment Operators
# ==============================

x = 10

x += 5
print("After += :", x)

x -= 5
print("After -= :", x)

x *= 2
print("After *= :", x)

x /= 2
print("After /= :", x)

x %= 3
print("After %= :", x)


# ==============================
# 5. Identity Operators
# ==============================

a = [1, 2, 3]
b = a

print(a is b)
print(a is not b)


# ==============================
# 6. Bitwise Operators
# ==============================

a = 5
b = 3

print("Bitwise AND:", a & b)
print("Bitwise OR:", a | b)
print("Bitwise XOR:", a ^ b)
print("Left Shift:", a << 1)
print("Right Shift:", a >> 1)


# ==============================
# 7. Membership Operators
# ==============================

text = "hello"

print("h" in text)
print("z" not in text)


# ==============================
# 8. if Statement
# ==============================

marks = 95

if marks >= 90:
    print("Excellent")


# ==============================
# 9. if-else Statement
# ==============================

marks = 90

if marks >= 90:
    print("You get a job")
else:
    print("You need to work harder")


# ==============================
# 10. if-elif-else Statement
# ==============================

marks = 87

if marks >= 90:
    print("You will get a phone")
elif marks >= 70:
    print("You will get a new book")
else:
    print("You will not get anything")


# ==============================
# 11. Nested if Statement
# ==============================

marks = 96

if marks >= 80:
    print("You passed")

    if marks >= 90:
        print("You can get a new phone")
    else:
        print("You can get a new book")


# ==============================
# 12. Short-hand if Statement
# ==============================

marks = 97

if marks >= 90:
    print("Good")


# ==============================
# 13. Short-hand if-else Statement
# ==============================

marks = 90

print("Good") if marks >= 90 else print("Needs improvement")
