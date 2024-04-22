"""
#24)
num = 250 # changed from 250 = num
while num <= 1000:
    if num >= 750: # changed the => to >=, syntax error
        print (num)
        num = num + 100
    else: # Added : to the end of else, syntax error
        print(num*2)
    num = num + 50 # indented this so that the while loop can function properly


#25)

val = 25 # changed from 25 = val
for i in range(0, val): # added : at the end of line
    if i % 2 == 0:
        print(i+1)
    else: #lower case e
        print(i-1) #added other ) to close statement


#26)

from functools import reduce
nums = [14, 17, -13, -75, 150, 15, 19, 10, -3, 16, 9, -145, 12, 50]
odd_nums = list(filter(lambda x: x%2 != 0, nums))
sub_odds = list(map(lambda x: x-5, odd_nums))
tot_sum = reduce(lambda a, b: a+b, sub_odds)
print(odd_nums)
print(sub_odds)
print(tot_sum)



#27)

file_obj = open('final.txt', 'r')
file_content = file_obj.readline()
print(file_content)

file_obj.close()


#28)

from util import squ_area
print(squ_area(5))

"""

#29)

import json
from dummy_json import collection
json_data = json.loads(collection)
print(json_data['product'])