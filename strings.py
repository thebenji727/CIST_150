'''
# don't use reserved keywords for variable names
print ('Hey world')
# ex. print = 'Jane'
print (help('keywords'))

# try to avoid multiple variable declaration simultaneously
a=10
b=10
c=10
print (a,b,c)
x = 47 # statement
y = x + 10 #expression
print (y)


#type conversion: change data type of variable
# can only convert floats and numeric strings to int
print(int('20'))
print(type(int('20')))
print(int(30))
print(int(14.12))

#print(int("20.24")) # errors out due to int expecting whole numbs inside quotes
print (int(float('20.24')))

## STRINGS ##
# 3 ways to make a string: using either single, double, or triple quotes
first_name = 'Jane'
last_name = "Doe"
address = "10 Main St."

job = "Physician Assistant" # recommended using double quotes for strings
# len () --> returns the numb of characters in a string
print (len("hello") )

# upper and lower coverts the case
print ("hello".upper())

# String concatenation - adding strings
age = 24
print(first_name+' '+last_name+ ": " + str(age))

## String multiplication - multiply strings with an it
print ("hello "*12)
'''

# accessing string characters - a sting is a sequence of characters

name = "Jane Doe"
print(name[2])
print (name[7])


# retrieving a character at a given index
print(name.index('o')) # returns 6
print(name.index('e')) # returns index of first appearance: 3
