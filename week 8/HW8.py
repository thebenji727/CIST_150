'''
#1)Write a function to check whether a given string or number is palindrome or not
def palindrome_check(str): #defines the function
    str_rev = str[::-1] #reverses the input string
    if str == str_rev: #checks if the reverse string is the same as the input string
        print('Palindrome')
    else:
        print('Not palindrome')

palindrome_check('Tuna') #performs function
###


#2)Write a function to check whether a given is string is anagram or not
def is_anagram(str1, str2): #defining the function, and the two strings that are inputed
    str1_sorted = sorted(str1) #sorts letters alphabetically in the form of A LIST
    str2_sorted = sorted(str2)

    if (str1_sorted == str2_sorted):  #checks if the two lists have the same letters and quantity of letters
        print('Anagrams')
    else:
        print ('Not Anagrams')

is_anagram('hello', 'leloh') #performs function
'''

#3)

def user_info (str1, num1, num2, num3):
    try:
        year = 2024
        age = year - num1
        name = str(str1)
        num_products = (num2 / num3)
        num_products_round = round(num_products, 0)
        print(name.isalpha())
        if name.isalpha() == False:
            print("That is not a name")
    except ZeroDivisionError as e:
        print("Error!", e)
    except ValueError as e:
        print("Error!", e)
    except Exception as e:
        print(e)
    else:
        print(f"Hello {name}! You are {age} years old and you can purchase {num_products_round} products.")

user_info(45, 1997, 300, 23)