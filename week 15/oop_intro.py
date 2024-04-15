
# Entity - something of interest which has properties and methods
# Class - template for an entity
# Object - copy created off of a template

class Student:
    #pass
    def __init__(self, first_name, last_name, score):
        self.first_name = first_name
        self.last_name = last_name
        self.email = f'{first_name}.{last_name}@gmail.com'
        self.score = score

    def fullname(self):
        return f"{self.first_name} {self.last_name}"


student3 = Student("Leeroy", "Jenkins", 85)
student4 = Student("Clark", "Kent", 97)
print(student3.email)
print(student4.email)

print(student3.fullname())
print(student4.fullname())

"""
student1 = Student()
student1.first_name = "Jane"
student1.last_name = "Doe"
student1.email = "jd@gmail.com"
student1.score = 85

student2 = Student()
student1.first_name = "John"
student1.last_name = "Moe"
student1.email = "jm@gmail.com"
student1.score = 95


print(student1)
print(student2)
"""

