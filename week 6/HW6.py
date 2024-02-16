'''
##1)
list_prime = []
prime_inp = int(input("Enter a number greater than 1: "))
if prime_inp <= 1:
     print("Enter a number greater than 1")
elif prime_inp == 2:
    list_prime.append(prime_inp)
else:
    for num in range(2, prime_inp):
        isPrime = True
        for i in range(2, num):
            if num % i == 0:
                isPrime = False
                break
        if isPrime is True:
            list_prime.append(num)
print(list_prime)


##2)
list_even = []
even_inp = int(input("Enter a number: "))
for num in range(1, even_inp+1):
    if num % 2 == 0:
        list_even.append(num)
print(list_even)




##3)
list = input("Enter numbers to be put in the list: ").split()
list2 = []
print("List: ", list)
ind_num = int(len(list))
for i in range(1,ind_num):
    if i % 2 == 1:
        num_i = int(i)
        odd_list = list[num_i]
        list2.append(odd_list)

print("List of numbers with odd indexes:", list2)
'''

##4)
list = input("Enter numbers to be put in the list: ").split()
int_list = 0
ind_num = int(len(list))
for num in range(1,ind_num):
    num_1 = int(num)
    num_2 = int(list[num_1])
    if num_2 > int_list:
        int_list = num_2
print("The largest number in the list is: ", int_list)