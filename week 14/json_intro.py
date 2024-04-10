# Java Script Object Notation
import json

emp_data ='''
{
    "employees": [
        {
            "name": "John",
            "age": 29,
            "email": ["jon@gmail.com", "john@outlook.con"]
        },
        {
            "name": "Jane",
            "age": 26,
            "email": null
        }
    ]

}
'''
import json
#to load json string into a python object
json_data = json.loads(emp_data)


'''
print(json_data)
print(type(json_data))
print(json_data['employees'])

for emp in json_data["employees"]:
    print(emp)



#Delete the email for each employee, then import it to a json string
for emp in json_data["employees"]:
    #del emp['email']
    pass


print(json_data)

#convert a python object to json string
new_string = json.dumps(json_data, indent=2)
print(new_string)
print(type(new_string))
'''

# how to load json data from a file into python object


"""
address ----> user entered address, recommended address
web application ----> USPS Public API ---> valid and return address


Fidelity Investments ---> Facebook page, twitter handle, linkedin
Facebook API - JSON Format
posts, comments, replies, etc.

"""

#import random
#random.random()
#random.choice()