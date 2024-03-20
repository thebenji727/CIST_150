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



# Iteration solution
ite_call_count = 0

def fib_val_it(fib_num):
    global  ite_call_count
    ite_call_count += 1
    if fib_num <= 1:
        return 1
    else:
        fib_list = [1, 1]
        for i in range(2, fib_num):
            fib_list.append(fib_list[i-1]+ fib_list[i-2])
        return fib_list[-1]

print(fib_val_it(10))


###LCS_RECURSION
def lcs_rec (A, B, i, j):
    if len(A) == 0 or len(B) == 0 or A[i] == '\0' or B[j] == '\0':
        #return 0
        return ""
    elif A[i] == B[j]:
        #return 1 + lcs_rec(A, B, i+1, j+1)
        return A[i] + lcs_rec(A, B, i+1, j+1)
    else:
        #return max(lcs_rec(A, B, i+1, j), lcs_rec(A, B, i, j+1))
        return max(lcs_rec(A, B, i+1, j), lcs_rec(A, B, i, j+1), key=len)

str1 = "bd"
str2 = "abcd"

str1 = str1 + "\0"
str2 = str2 + "\0"

for _ in range(len(str1)):


#seq_len = lcs_rec(A=str1,B=str2,i=0,j=0)
#print(seq_len)

lcs_char = lcs_rec(A=str1, B=str2, i=0, j=0)
print(lcs_char)

# the #ed out code prints the NUMBER of similar charaters in the string
'''

# LCS_MEMOIZATION
def lcs_memoization(A, B, i, j):
    global lcs_memo
    global calls
    calls += 1
    if len(A) == 0 or len(B) == 0 or A[i] == '\0' or B[j] == '\0':
        return 0
    if lcs_memo[i][j] == " ":
        if A[i] == B[j]:
            lcs_memo[i][j] = 1 + lcs_memoization(A, B, i+1, j+1)
        else:
            lcs_memo[i][j] = max(lcs_memoization(A, B, i+1, j), lcs_memoization(A, B, i, j+1))
    return lcs_memo[i][j]

calls = 0
str1 = "bd"
str2 = "abcd"

str1 = str1 + "\0"
str2 = str2 + "\0"

lcs_memo = []

for _ in range(len(str1)):
    lcs_memo.append([" "] * len(str2))

print(lcs_memo)
seq_len = lcs_memoization(A=str1, B=str2, i=0, j=0)
print(seq_len)
print(calls)