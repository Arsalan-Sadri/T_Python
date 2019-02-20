# __repr__()
    # Gets called behind the scene when obj is getting printed

# __str__()
    # Gets called behind the scene when obj is getting printed
    # So, you can override it to behave the way you like it 
    # If there is an implementation of __repr__(), this __str__()
    # takes priority

# __add__()
    # Gets called behind the scene when 2 objects of the same type
    # are combined via plus + sign operator 

class Employee: 

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def full_name(self):
        return "{} {}".format(self.first, self.last)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)
    
    def __str__(self):
        return "Employee('{} {}')".format(self.first, self.last)
    
    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.full_name())


emp_1 = Employee("Sheldon", "Adelson", 600000)
emp_2 = Employee("Donald", "Trump", 400000)
emp_3 = Employee("Michael", "Avenatti", 1000000)

print(emp_1)                                # >> Employee('Sheldon Adelson')

print(emp_1 + emp_2)                        # >> 1000000

print(len(emp_3))                           # >> 16


