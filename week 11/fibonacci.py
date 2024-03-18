## Recursive solution
'''
rec_call_count = 0

def fibo_num_rec (fib_num):
    global rec_call_count ### Function now understands that it needs to call something outside of itself
    rec_call_count += 1
    if fib_num <=1:
        return fib_num
    else:
        return fibo_num_rec(fib_num - 2) + fibo_num_rec(fib_num - 1)

for num in [5, 10, 15, 20, 25, 30, 35, 40]:
    rec_call_count = 0
    print(f"{num}th value is {fibo_num_rec(num)}")
    print(f"Total function calls: {rec_call_count:,}")
    print("*"*500)
    print()
'''

## Memoization solution


fib_val_mem = {}
rec_call_count = 0

def fib_num_mem(fib_num):
    global fib_val_mem
    global rec_call_count
    rec_call_count += 1
    if fib_num in fib_val_mem:     ## if this value is in the dictionary, just return the number
        return fib_val_mem[fib_num]

    elif fib_num <= 1:
        fib_val_mem[fib_num] = fib_num

    else:
        fib_val_mem[fib_num] = fib_num_mem(fib_num-2) + fib_num_mem(fib_num-1)
    return fib_val_mem[fib_num]

for num in [5, 10, 15, 20, 25, 30, 35, 40]:
    rec_call_count = 0
    print(f"{num}th value is {fib_num_mem(num)}")
    print(f"Total function calls: {rec_call_count:,}")
    print("*"*500)
    print()