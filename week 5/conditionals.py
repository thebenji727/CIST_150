"""
### If-Else

height = int(input("enter your height in cms: "))
if height >= 120:
    print("Congrats! You can ride the coaster!")
else:
    print("I'm sorry, you cant ride the coaster...")



## Nested If-Else
#1)
height = int(input("enter your height in cms: "))
age = int(input("enter your age: "))
if height >= 120:
    print("Congrats! You can ride the coaster!")
    if age > 18:
        print("The price for your ticked will be $12")
    else:
        print("The price for your ticket is $7")
else:
    print("I'm sorry, you cant ride the coaster...")


# 2)
height = int(input("enter your height in cms: "))
age = int(input("enter your age: "))
photo_inp = input("Do you want a ticket?")
total_price = 0
if height >= 120:
    print("Congrats! You can ride the coaster!")
    if age >= 18:
        tic_price = 12
        print("The price for your ticked will be $12")
    elif 12 <= age < 18:
        tic_price = 7
        print("The price for your ticket is $7")
    else:
        tic_price = 5
        print("The price for your ticket is $5")

    if photo_inp == "Y" or photo_inp == "y":
        total_price = tic_price + 3
    print("The total for the bill will be: " + "$" + str(total_price))
else:
    print("I'm sorry, you cant ride the coaster...")


#3)
height = int(input("enter your height in cms: "))
age = int(input("enter your age: "))
photo_inp = input("Do you want a photo?")
total_price = 0
if height >= 120:
    print("Congrats! You can ride the coaster!")
    if 45<= age < 55:
        tic_price = 0
        print("The price for your ticket will be $0!")
    elif age >= 18:
        tic_price = 12
        print("The price for your ticked will be $12")
    elif 12 <= age < 18:
        tic_price = 7
        print("The price for your ticket is $7")
    else:
        tic_price = 5
        print("The price for your ticket is $5")

    if photo_inp == "Y" or photo_inp == "y":
        total_price = tic_price + 3
    print("The total for the bill will be: " + "$" + str(total_price))
else:
    print("I'm sorry, you cant ride the coaster...")

"""

#4)

grade_percent = int(input("Please enter your grade percentage:"))
if grade_percent < 60:
    letter_grade = 'F'
    print("Your grade is " + letter_grade)
elif grade_percent < 70:
    if grade_percent <= 63:
        letter_grade = 'D-'
        print("Your grade is " + letter_grade)
    elif grade_percent < 67:
        letter_grade = 'D'
        print("Your grade is " + letter_grade)
    else:
        letter_grade = 'D+'
        print("Your grade is " + letter_grade)
elif grade_percent < 80:
    if grade_percent <= 73:
        letter_grade = 'C-'
        print("Your grade is " + letter_grade)
    elif grade_percent < 77:
        letter_grade = 'C'
        print("Your grade is " + letter_grade)
    else:
        letter_grade = 'C+'
        print("Your grade is " + letter_grade)
elif grade_percent < 90:
    if grade_percent <= 83:
        letter_grade = 'B-'
        print("Your grade is " + letter_grade)
    elif grade_percent < 87:
        letter_grade = 'B'
        print("Your grade is " + letter_grade)
    else:
        letter_grade = 'B+'
        print("Your grade is " + letter_grade)
elif grade_percent <= 100:
    if grade_percent <= 93:
        letter_grade = 'A-'
        print("Your grade is " + letter_grade)
    elif grade_percent < 97:
        letter_grade = 'A'
        print("Your grade is " + letter_grade)
    else:
        letter_grade = 'A+'
        print("Your grade is " + letter_grade)


