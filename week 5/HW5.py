# 1)
"""
int_dict = {
    0: 'Zero',
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four',
    5: 'Five',
    6: 'Six',
    7: 'Seven',
    8: 'Eight',
    9: 'Nine'
}
num = int(input("Enter a single digit: "))
print(int_dict[num])


int_list = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
num = int(input("Enter a single digit: "))
print(int_list[num])


# 2)
user_rps = input("Please choose between rock, paper, or scissors: ")
cpu_rps = ''
import random
rand_num = random.random() #prints a random number between 0 and 1
dig_rand = (round(rand_num, 2)) #rounds up to 2 digits ie 0.34567 -> 0.3
if dig_rand >= 0 and rand_num < 1/3:
    cpu_rps = "rock"
elif 1/3 >= dig_rand < 2/3:
    cpu_rps = "paper"
else:
    cpu_rps = "scissors"
#print("Computer: " + cpu_rps)
#print("User: " + user_rps)
result = ''
if user_rps == cpu_rps:
    result = "It's a tie."
elif user_rps == 'rock':
    if cpu_rps == "paper":
        result = "You lose..."
    else:
        result = "You win!"
elif user_rps == 'paper':
    if cpu_rps == "scissors":
        result = "You lose..."
    else:
        result = "You win!"
elif user_rps == 'scissors':
    if cpu_rps == "rock":
        result = "You lose..."
    else:
        result = "You win!"
print(f"You picked {user_rps}, and the computer picked {cpu_rps}. {result}")

"""
# 3)
year_inp = int(input("Please input a year to see if its a leap year: "))
leap_inp = year_inp%4 # % is a modulus operator
if year_inp%4 == 0:
    if year_inp%100 == 0:
        if year_inp%400 == 0:
            result = "That's a leap year!"
        else:
            result = "That's not a leap year"
    else:
        result = "That's a leap year!"
else:
    result = "That's not a leap year"
print(result)

#4)

