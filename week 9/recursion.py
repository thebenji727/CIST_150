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
'''
