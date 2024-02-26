##Functions - reusable blocks of code
##write a function to check if a number is odd or even
def checkEven(num):
    result = ''
    if num % 2 == 0:
        result = True
    else:
        result = False
    return result
print(checkEven(49)) # 4 --> function arguments

is_even = checkEven(234590123095822345634)
print(is_even)

'''
print("Hello") # does not have any return type
import random
rand_num = random.random() # has a return type, needed to be captured as a variable
'''