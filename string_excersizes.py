'''

name=input('Input a word to be scrambled \n')
print("Cutting and scrambling word... \n")
str_length = len(name)
middle = str_length/2
midint=int(middle)
mid_char= name[midint]
print (name[0]+ mid_char+name[-1])



name = input("Input a word to be scrambled \n")
str_length = len(name)

midM = str_length/2
midM1 = (str_length/2)+1
mid1M = (str_length/2)-1

midinitM = int(midM)
midinitM1 = int(midM1)
midinit1M = int(mid1M)

midM_char = name[midinitM]
midM1_char = name[midinitM1]
mid1M_char = name[midinit1M]

print(mid1M_char + midM_char + midM1_char)




name1 = input("Input a word to be cut in half \n")
name2 = input("Input a word to be put in the middle \n")

str_length = len(name1)
middle = str_length/2



# string slicing
emp_name = "Leeroy Jenkins"
print(emp_name[2:6]) # prints "eroy"
print(emp_name[0:4])
print(emp_name[:6]) # prints "Leeroy"
print(emp_name[7:]) # prints "Jenkins"
print(emp_name[-4:-1]) # prints "kin"
print(emp_name[1:6:2]) # prints "ery"
print(emp_name.count('e')) # counts how many times a character appears on the string
print(emp_name.find('Jenkins')) # prints 7, shows position where substring is located
print(emp_name.replace('Leeroy', 'Royler')) # replaces, not permanent though

# emp_name = emp_name.replace(...) replaces and makes change permanent
print('ee' in emp_name) # checks if the characters are IN the string


'''

##STRING FORMATING
student_name = "Alex"
score = 74

print("Name: " + student_name + '  '+ "Score: " + str(score) )
print("name: {} Score: {}".format(student_name,score))


# F-stings

print(f'Name: {student_name} Score: {score}')
print(f"3 times 10 is {3*10}")