# Class properties/attributes
    # Unlike Java, they are not defined explicitly
    # They are defined as params of the class constructor and
    # get initialized when the constructor is called 
    
# In object instantiation, when a constructor is called via
# <obj> = <Class(params)>, a reference/pointer representing the object
# automatically gets created and passed to its constructor. 
# By convention, this is called "self".
# This reference also automatically gets passed to each non-static method
# of the class. 
# Each method needs to take this instance as its first argument
# __init__() is the class constructor
# A class properties are not explicitly defined, but they are defined
# as a part of __init()__ constructor's parameters 
# These properties can be accessed via <instance>.<property>
# Properties might be further added via <instance>.<property> = <value>
# Use <object>.__dict__ to see all attributes of an object in a form of a 
# dictionary object 


class Employee:
    
    def __init__(self, first, last, email):
        self.first = first
        self.last = last
        self.email = email
    
    def full_name(self):
        return "{} {}".format(self.first, self.last)


emp = Employee("Arsalan", "Sadri", "a.sadri@company.com")

print(emp.__dict__)

print(emp.first)
print(emp.last)
print(emp.email)

emp.age = 56
print(emp.age)

print(emp.full_name())
print(Employee.full_name(emp))

