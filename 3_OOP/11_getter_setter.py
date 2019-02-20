# @property
    # We define a method and have it decorated with @property
    # This allows to access a class method as if it were a class property.
    # That is, when calling the method, there will no longer be any paranthesis
    
# <method_property_name>.setter
    # Use setters to assign a value to a method property
    # The method must have already been defined and decorated with @property

# <method_property_name>.deleter
    # deleters are used in conjunction with del operator 
    # The method property must have already been defined and decorated with @property
    

class Person:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def get_email(self):
        return "{}.{}@email.com".format(self.first.capitalize(), self.last.capitalize())
    
    @property
    def full_name(self):
        return "{} {}".format(self.first, self.last)

    @full_name.setter
    def full_name(self, f_name):
        self.first, self.last = f_name.split(" ")
    
    @full_name.deleter
    def full_name(self):
        self.first = None
        self.last = None
        print("Name deleted!")
        

per = Person("Wolf", "Blitzer")

# Accessing the get_email() method as a property
print(per.get_email)

# Accessing the full_name() method as a property
print(per.full_name)

# Setting the first and last name via property setter 
per.full_name = "David Attenborough"
print(per.full_name)

# Deleting the full_name property
del per.full_name
print(per.full_name)