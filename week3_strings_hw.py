'''
#question 1

week 3 excersizes

##Q1 & 2

input_str = input("Please enter a string: ")
print(input_str)
mid_index = int (len(input_str)/2)

res_str = input_str[mid_index-1:mid_index+2]
print(res_str)



Please enter a string: Whatever
Whatever
tev
 ###commands asks for a sting to be inputed, after that the string is the printed back out. the next lines in the program calls for the program to find the middle value of the string (in terms of the string's length). After that the program then is tasked with printing out the value at the middle and the ones before and after it.

##Q3


str1 = input("Please enter a string: ")
str2 = input("And the second string?: ")
print(str1)
mid_str1 = int(len(str1)/2)
firsthalf = str1[:mid_str1:1]
firsthalf = firsthalf + str2
final_str = firsthalf + str1[mid_str1:]
print(final_str)
### first 2 steps as for the user to input 2 strings, the next line then prints out the first string. then the program is tasked with finding the middle point of the string. After that the program then stores the first half by storing all the characters from the start of the string to the point in the middle and stores it as a new string. Now the program adds the second string to the end of the first, and finally the program adds the remaining part of the first string (by checking all the characters after the mid point) to the end of the already combined string

##Q4


str = input("Please enter a string: ")
print(str)
rev_str = str[::-1]
print(rev_str)
 ### The program asks for a string to be input. After that the program then prints the string as it is, then the program creates a new string by slicing the first string after each character but starting at the end (hence why the -1 is used). Then the program is then made to print the new string

##Q5

given_str = "The total value of the 10 products purchased along with the tax is $150"
print(given_str[-3:])
 ###The program is given a string and the 2nd line ask for the characters in the string from the 3rd to last to the end.

##Q6

str1 = "Hello there world~!"
print(str1)
new_char = "Z"
new_str = str1[:3]+new_char+str1[3+1:]
print(new_str)
 ### First 2 lines are the string and printing the string. The next line is then the replacement character, the the program makes a new string by adding the new charater where the cut was made.


#question 2

inp_first = input("Please give your first name. \n")
inp_last = input("Please give your last name. \n")
inp_age = input("Please give your age. \n")
inp_SSN = input("Please give your SSN. \n")
inp_height = input("Please give your height in cm. \n")
inp_weight = input ("Please give your weight in lbs. \n")

print("Hello "+ inp_first + " " + inp_last + "! Thank you for applying! Please find your details below!")
print("   Age:" + inp_age)
print("   SSN:" + inp_SSN)
height_cm = int(inp_height)
height_in = height_cm/2.54
int_h= int(height_in)
print("   Height:"+ str(int_h)+" Inches")
weight_lbs = int(inp_weight)
weight_kg = weight_lbs * 0.45
int_w = int(weight_kg)
print("   Weight:" + str(int_w)+ " Kgs")


#question 3

quote = "You have brains in your head. You have feet in your shoes. You can steer yourself any direction you choose. -Dr. Seuss"
print(quote)
quote.replace("steer yourself any direction you choose", '')
print(bool(quote.find('feet')))
print(quote.replace("Dr. Seuss","Dr. Seuss, Oh the Places You'll Go!"))

'''