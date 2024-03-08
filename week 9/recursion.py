# process that a function calls itself so long as a certain condition is satisfied.
'''
def sayHello(name):
    print(f"Hello {name}!")

def userDetails():
    username = input("Enter a name: ")
    sayHello(username)
    usercity = input("Enter a city: ")
    print(f"You are from {usercity}")

userDetails()


def test1(n):
    if (n > 0):
        print("printing the value: ")
        print(n)
        print("calling the function...")
        test1(n-1)

test1(3)


def test2(n):
    if (n > 0):
        print("calling the function...")
        test2(n-1)
        print("printing the value")
        print(n)

test2(3)

# ***ordered in stack memory, it prints 1 then 2 then 3



# write program to find factorial of number
# ex = 5! = 5*4*3*2*1 = 120

def factorialnum(n):
    if n < 0:
        print("Please input a positive number")
        return
    elif (n <= 1):
        return 1
    else:
        return n * factorialnum(n-1)

fact_val = factorialnum(5)
print(fact_val)

import statistics

def quicksort(num_list):
    if len(num_list) <= 1:
        return num_list
    else:
        #find median
        median_val = statistics.median([num_list[0], num_list[len(num_list)//2], num_list[-1]])
        list1 = []
        list2 = []
        list3 = []
        for i in num_list:
            if i < median_val:
                list1.append(i)
            elif i > median_val:
                list3.append(i)
            else:
                list2.append(i)
        return(quicksort(list1) + list2 + quicksort(list3))


sort_list = quicksort([31, 18, 72, 79, 3, 18, 92, 11, 44, 56, 41, 28])
print(sort_list)
'''

def FiboSequence(num):
    if num <=0: #to make sure that we start the sequence with a positive number and not a 0 or a negative one
        print("Please put in a number greater than 0...")
    elif num == 1:          #these first two elif statements are for the unique cases in the fibonnachi sequence since the first 2 numbers are 1 and 1
        return [1]
    elif num == 2:
        return [1, 1]
    else:                   #the actual code for the sequence
        fib_list = [1, 1]
        for i in range(2, num):
            fib_list.append(fib_list[i-1] + fib_list[i-2])
        return fib_list

print(FiboSequence(30))

