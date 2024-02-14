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
'''

##2)
list_even = []
even_inp = int(input("Enter a number: "))
for num in range(1, even_inp+1):
    if num % 2 == 0:
        list_even.append(num)
print(list_even)

