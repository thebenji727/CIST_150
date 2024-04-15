import logging
## 5 types of information that you can log: DEBUG, INFO, WARNING, ERROR, CRITICAL



def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def mutliply (x, y):
    return x * y

def divide (x, y):
    return x / y



num1 = 10
num2 = 5

"""
add_res = add(num1, num2)
logging.warning(f' Add: {num1} + {num2} = {add_res}')

sub_res = subtract(num1, num2)
logging.debug(f' Subtract: {num1} + {num2} = {sub_res}')



#changing the default logging level from logging to debug
#logging.basicConfig(level=logging.DEBUG)


add_res = add(num1, num2)
logging.warning(f' Add: {num1} + {num2} = {add_res}')

sub_res = subtract(num1, num2)
logging.debug(f' Subtract: {num1} + {num2} = {sub_res}')
"""


logging.basicConfig(filename='log_sample.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

multi_res = mutliply(num1, num2)
logging.warning(f' Multiply: {num1} * {num2} = {multi_res}')

div_res = divide(num1, num2)
logging.debug(f' Divide: {num1} / {num2} = {div_res}')
