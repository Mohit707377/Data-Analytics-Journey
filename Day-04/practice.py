# Day 04 - Problem Solving


# Question 1:
# Write a program to check whether a number is positive or not.

'''
num = int(input("Enter the number :- "))

if num > 0:
    print(num, "is a positive number")
else:
    print(num, "is not a positive number")
'''


# Question 2:
# Write a program to check whether a number is even or odd.

'''
num = int(input("Enter the number :- "))

if num % 2 == 0:
    print(num, "is an even number")
else:
    print(num, "is an odd number")
'''


# Question 3:
# Make an Area Calculator.

'''
print("++++++++++++++++++++++++++++++++++")
print("+      1 -> Area of Rectangle    +")
print("+      2 -> Area of Triangle     +")
print("+      3 -> Area of Square       +")
print("+      4 -> Area of Circle       +")
print("++++++++++++++++++++++++++++++++++")

choice = int(input("Enter your choice :- "))

if choice == 1:
    leng = int(input("Enter the length of rectangle :- "))
    breg = int(input("Enter the breadth of rectangle :- "))

    area_rec = leng * breg

    print("Area of rectangle is", area_rec)

elif choice == 2:
    breg = int(input("Enter the base of triangle :- "))
    heig = int(input("Enter the height of triangle :- "))

    area_tri = 1 / 2 * breg * heig

    print("Area of triangle is", area_tri)

elif choice == 3:
    side = int(input("Enter the side :- "))

    area_sq = side ** 2

    print("Area of square is", area_sq)

elif choice == 4:
    radius = int(input("Enter the radius :- "))

    area = 3.14 * radius ** 2

    print("Area of circle is", area)

else:
    print("Invalid choice !!!!")
'''


# Question 4:
# Write a program to check whether a letter is a vowel or not.

'''
letter = input("Enter the letter :- ")

if (letter in "aeiou") or (letter in "AEIOU"):
    print("It is a vowel")
else:
    print("It is not a vowel")
'''


# Question 5:
# Write a program to check whether a number is single-digit,
# double-digit, triple-digit, or four-digit.

'''
num = int(input("Enter the number here up to 4 digit :- "))

if num >= 0 and num <= 9:
    print("Number is single digit")

elif num >= 10 and num <= 99:
    print("Number is double digit")

elif num >= 100 and num <= 999:
    print("Number is triple digit")

elif num >= 1000 and num <= 9999:
    print("Number is four digit")

else:
    print("Invalid !!!")
'''
