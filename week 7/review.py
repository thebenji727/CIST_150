'''
for i in range(11):
    if i % 2 ==0:
        continue
    else:
        print(i)


### Write a program to calculate the sum and average of digits in a string
sum_list = 0
count = 0
str_inp = input("Enter a string with random numbers, letters and symbols: ")
for char in str_inp:
    if char.isdigit():
        char_num = int(char)
        count = count + 1
        sum_list = sum_list + char_num
    else:
        continue
avg = sum_list/count
print(f'Number of digits: {count}, and sum of those digits is: {sum_list}, the average is: {round(avg,2)} ')



dig_num = 0
char_num = 0
sym_num = 0
str_inp = input("Enter a string with random numbers, letters and symbols: ")
for char in str_inp:
    if char.isdigit():
        dig_num = dig_num +1
    elif char.isalpha():
        char_num = char_num + 1
    elif char.isascii():
        sym_num = sym_num + 1
print(f"Number of digits: {dig_num}, number of characters: {char_num}, number of symbols {sym_num}")

line_num = int(input("Please enter a number of lines to be printed: "))
for i in range(0,line_num):
    for j in range(i+1):
        print(j*2, end= ' ')
    print()
'''
random_val = 0
guess_num = 1
import random
rand_num = random.random()
dig_rand = int((round(rand_num,1))*10)
random_val = random_val + dig_rand

cont_inp = "Y"
while cont_inp.lower() == "y":
    user_inp = int(input("Guess a number: "))
    if guess_num > 5:
        print(f"You took too long. The right answer was {random_val}")
        break
    else:
        if user_inp > random_val:
            guess_num = guess_num + 1
            print("Too high! Try again!")
        elif user_inp < random_val:
            guess_num = guess_num + 1
            print("Too low! Try again!")
        elif random_val == user_inp:
            print(f"You got the right number, it was {random_val}, the number of times you guessed was: {guess_num}")
            break
    cont_inp = input("Do you want to continue Y/N? ")
