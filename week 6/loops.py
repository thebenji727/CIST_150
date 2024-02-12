#### While Loops
'''
x = 1
while x < 5: # loop variable - x
    print(x)
    x = x + 1
    # x += 1

y = 0
while y < 10:
    print(y)
    y += 1



cont_inp = "Y"
while cont_inp.lower() == "y":
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
    cont_inp = input("Do you want to continue Y/N? ")

print("Thanks for playing!~")


### Break: loop stops

#y = 0
#while y <= 10:
#    if y == 3:
#        break
#    print(y)
#    y += 1
#prints 0,1,2. Loop stops


### Continue

#y = 0
#while y <= 10:
#    if y == 3:
#        continue
#    print(y)
#    y += 1
#prints 0,1,2. Loop continues to run even after the condition is met


#### For Loops

num_list = [1,2,3,4,5,6]
for num in num_list:
    print(num+10)


### Range - internally makes a list up until the value given
# Can have a starting value, ending value, step
for i in range(1, 10, 2): #starting value is 0, ending value isn't included
    print(i)

#y = 0
#list_y = []
#while y <= 10:
#    y += 1
#    list_y.append (y)
#print(list_y)

sum = 0
for i in range(6):
    print('sum: ' , sum)
    print ("i: ", i)
    sum = sum + 1
print(sum)


inp_tbl = int(input("please input an integer to make a multiplication table: "))
for i in range(1, 11):
    inp_tbl_out = inp_tbl * i
    print(inp_tbl, "times", i, "is", inp_tbl_out)

### Nested Loops - loops within loops
for num in [1,2,3]:
    for letter in 'abc':
        print(num, letter)


y = int(input("Input an integer: "))
x = 0
list_y = []
for i in range(y):
    x += 1
    list_y.append(x)
    print(list_y)
'''
rows = int(input('Enter the # of rows: '))
for i in range(1, rows+1):
    for j in range(1, i+ 1):
        print(j, end='')
    print()