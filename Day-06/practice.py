# Day 06 - Python Loops & String Problem Solving

# LOOP PROBLEM SOLVING



# 1. Sum of Even Numbers up to 50

sum_even = 0

for i in range(1, 51):
    if i % 2 == 0:
        sum_even = sum_even + i

print("Sum of even numbers up to 50:", sum_even)


# 2. Square of First 20 Numbers

for i in range(1, 21):
    print("The square of", i, "is", i ** 2)


# 3. Sum of First 10 Odd Numbers using while Loop

n = 0
sum_odd = 0
count = 0

while True:
    if n % 2 != 0:
        sum_odd = sum_odd + n
        count += 1

    n += 1

    if count == 10:
        break

print("Sum of first 10 odd numbers:", sum_odd)


# 4. Billing System

while True:
    name = input("Enter your name: ")
    total = 0

    while True:
        print("\nEnter the Amount and Quantity")

        quantity = int(input("Enter the Quantity: "))
        amount = int(input("Enter the Amount: "))

        total += amount * quantity

        con = input("Do you want to add something more (yes or no): ")

        if con.lower() == "no":
            break

    print("-" * 40)
    print("Customer:", name)
    print("Bill is:", total)
    print("******** Happy Shopping ********")
    print("-" * 40)

    con2 = input("Do you want to go to next customer? (yes or no): ")

    if con2.lower() == "no":
        break


# STRING PROBLEM SOLVING

a = "Why fit in,When you are Born to Stand Out !"

# 1. Find the Length of String

print("The length of String is:", len(a))


# 2. Count Occurrence of 'o'

print("o is occurring", a.count("o"), "times")


# 3. Convert String into Lowercase

x = a.lower()
print("Lowercase:", x)


# 4. Convert String into Uppercase

y = a.upper()
print("Uppercase:", y)


# 5. Convert String into Title Case

z = a.title()
print("Title Case:", z)


# 6. Find the Index of "fit in"

print("The index of 'fit in' is:", a.find("fit in"))
