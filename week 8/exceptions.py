### Exception - unwanted scenario that disrupts the normal flow o your program

'''
#Normal statements
a = 5
b = 0

try:
    #critical statements
    print(a/b)
except Exception:
    print("Oopsy poopsy, the code did a fucky wucky")
print('End')

try:
    print('Connection opened')
    inp_1 = int(input('Enter the first number: '))
    inp_2 = int(input('Enter the second number: '))
    result = inp_1 / inp_2
except ZeroDivisionError as e:
    print("Oopsy poopsy, you did a fucky wucky:", e)
except ValueError as e:
    print("Oopsy poopsy, you did a fucky wucky:", e)
except Exception as e:
    print("Oopsy poopsy, you did a fucky wucky:", e)
else:
    print(f"The result of {inp_1} divided by {inp_2} is {result}") #would run only if there are no errors thrown from the try block
finally: #used to the code that NEEDS to be executed no matter if there's an error or not
    print("Connection terminated")
'''

num_list = [1, 2, 3, 4, 0, 5, 6]
for num in num_list:
    try:
        result = 10 / num
    except ZeroDivisionError as e:
        print(e)
    except Exception as e:
        print(e)
    else:
        print(result)