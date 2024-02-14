num_3 = str("fizz")
num_5 = str('buzz')
target_num = int(input('Enter a target: '))
for num in range(1, target_num+1):
    if num % 3 == 0 and num % 5 == 0:
        print(num_3 + num_5)
    elif num % 3 == 0:
        print(num_3)
    elif num % 5 == 0:
        print(num_5)
    else:
        print(num)