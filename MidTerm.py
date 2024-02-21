'''

##1)
cont_inp = "Y"
while cont_inp.lower() == "y":
    import random
    rand_num = random.random()
    dig_rand = (round(rand_num, 1))
    num_rand = int(dig_rand * 10)

    if num_rand % 2 == 0:
        coin_cpu = str('heads')
    else:
        coin_cpu = ('tails')
    coin_user = input("Pick heads or tails: ")
    if coin_user.lower() == coin_cpu:
        print(f"you chose {coin_user} and the computer chose {coin_cpu} its a tie!")
    elif coin_user.lower() == 'heads' and coin_cpu == 'tails':
        print(f"you chose {coin_user} and the computer chose {coin_cpu} you win!")
    elif coin_user.lower() == 'tails' and coin_cpu == 'heads':
        print(f"you chose {coin_user} and the computer chose {coin_cpu} you lose!")
    cont_inp = input("Do you want to continue Y/N? ")


##2)
list_1 = [12 , 75, 150, 180, 145, 525, 50]
list_2 = []
for num in list_1:
    if num % 5 == 0 and num <= 150:
        list_2.append(num)
    elif num > 150:
            continue
    elif num > 500:
            break

print(list_2)


##3)
line_num = int(input("Please enter a number of lines to be printed: "))
for i in range(0,line_num):
    for j in range(i+1):
        print((j*2)+1, end= ' ')
    print()
'''


##4)

fact_inp = int(input("Input a number: "))
fact_list = []
for i in range(1, fact_inp+1):
    if fact_inp % i == 0:
        fact_list.append(i)
print(f"the factors of {fact_inp} are: {fact_list}")


