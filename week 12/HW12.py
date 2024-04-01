##1)
prduct_num = lambda a, b: a * b
print(prduct_num(3,5))

##2)
diff_num = lambda a,b : a-b
print((lambda a,b : a-b)(5,3))

##3)
nums = [3, 2, 6, 8, 4, 6, 2, 9]
great5_num = filter(lambda x: x > 5, nums)
print(list(great5_num))

##4)
num5_check = lambda num: num/5 if num > 10 else num+5
print(num5_check(15))

##5)
list5 = [3, 2, 6, 8, 4, 6, 2, 9]
double_list = map(lambda n: n*2, list5)
print(list(double_list))

##6)
from functools import reduce
list_6 = [3, 2, 6, 8, 4, 6, 2, 9]
odd_nums = list(filter(lambda x: x%2 != 0, nums))
print(odd_nums)

squ_list = list(map(lambda x: x*x, odd_nums))
print(squ_list)

def addall (a,b):
    return a+b
tot_sum = reduce(addall, squ_list)
print(tot_sum)