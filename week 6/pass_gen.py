import random

list_let = list('abcdefghijklmnopqrstuvwxyz')
list_num = list('0123456789')
list_sym = list('!?@#$%^&*')

num_let = int(input('How many letters do you want?: '))
num_num = int(input('How many numbers do you want?: '))
num_sym = int(input('How many symbols do you want?: '))
password_char = []
for letter in range(0, num_let):
    password_char.append(random.choice(list_let))

for digit in range(0, num_num):
    password_char.append(random.choice(list_num))

for num_sym in range(0, num_sym):
    password_char.append(random.choice(list_sym))
print(password_char)
random.shuffle(password_char)
print(password_char)
password = ''.join(password_char)
print(password)