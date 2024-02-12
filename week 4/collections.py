'''
### LISTS []
#### KEY POINTS:
# 1) allow duplicate data
# 2) order is maintained
# 3) allows heterogeneous data

list1 = [10, 'test', False, 23.24]
print(list1)

print(len(list1))

### Allows indexing and slicing
print(list1[2])
print(list1[1:4])
print(list1[-2])

### Can hold other lists too
list2 = [34, 23.65, "hello", True, ["Hello", 45, False]]
print(list2[4][1]) ## Prints '45'

### Creating an empty list
country = [] ##initalizes an empty container
### new elements can be added to the list by using append, insert, or extend.
country.append('Germany')
country.append('France')
country.append('Canada')
country.append('France')
country.append('Sri Lanka')
print(country) ## Append always adds elements at the end of the list

country.insert (2, "Mexico") ## adds an element to the list at a specific location
print(country)
country2 = ['China','Denmark','USA']
country.extend(country2) #extend is an inplace function, changes the object internally but doesn't return anything
#print(country)
#country.append(country2)
#country.pop()
print(country)
#print(country)
##Sort Functions
country.sort()
print(country)
country.sort(reverse=True)
print(country)



###Membership test
print('USA'in country) #True
country_str = '-'.join(country)
print(country_str)
print(type(country))
print(type(country_str))


##String to list!
country3 = country_str.split('-')
print(country3)

##Tuples  () ##

## 1) Can't be modified (cant update, add, or remove elements)

tuple1 = (12, 234, 5123, 12.3) ##***** they use (), not []
print(tuple1[2])

###SETS {}
# 1) Dont allow dups
# 2) Order isnt garunteed
courses1 = {"English", "History", "Mythology", "History", "Science"}
print(courses1)

### Set operations
courses2 = {"Math", "Data Analytics", "English", "Economics"}
print(courses1.union(courses2))
print(courses1.intersection(courses2))
print(courses1.difference(courses2))
print(courses2.difference(courses1))

'''
##### Dictionaries ####
#emp1 = {
#    "id": 1233,
#    "name": "John",
#    "Skills": ["Java", "PHP", "Python"],
#    "Address": {
#        "City": "LA",
#        "State": "CA",
#        "ZIP": 19210
#    }
#}
#print(emp1['Address']['State'])

emp_dict = [
    {
        "id": 1233,
        "name": "John",
        "Skills": ["Java", "PHP", "Python"],
        "Address": {
            "City": "LA",
            "State": "CA",
            "ZIP": 19210
        }
    },
    {
        "id": 1234,
        "name": "Davis",
        "Skills": ["Magic", "Wizardry", "Sorcery"],
        "Address": {
            "City": "San Diego",
            "State": "CA",
            "ZIP": 19210
        }
    }
]
print(emp_dict[1]["Skills"][1])

### Converting lists and tuples to sets ###
list2 = [11, 12, 12, 13, 14, 15, 16, 17, 18, 19]
set2 = set(list2) #also pass a tuple
print(set2)
##### Creating Empty Collections
#list1 = []
#tuple1 = ()
#set1 = {}
# print(type(set1))
#dict1= {}
#set1 = set()
#tuple1 = (10,)
#print(type(tuple1))
 ### ACCESSING ELEMENTS FROM COLLECTIONS ###
#list1 = [32, 423, 5, [123, 2345, 26], [35, 36, 2, [10, 11, 12], 13]] # make it print the 10
#print(list1[4][3][0]) # prints "10"
### Tuples also support indexing and slicing, similar to as above^

#set1 = {234, 345, 456}
#print(set1[1])
# Set doesnt assign set positions/they are unordered, can not support indexing and sclicing
