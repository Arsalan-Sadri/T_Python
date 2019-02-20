# INHERITANCE
    # The idea is to inherit a base model, then add on top of that or alter 
    # the inheritted one without affecting the super-class.
    # method resolution order: __init()__ is not in the developer,
    # Python walks up the chain of inheritance to find it. 
    # you can see those stuff from help(<class_name>)

class Employee: 

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def full_name(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


emp = Employee("John", "Doe", 80000)


class Developer(Employee):
    
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


dev = Developer("Arsalan", "Sadri", 100000, "Python")

print(dev.__dict__)

# Altering raise_amt in Developer only
dev.apply_raise()
print(dev.raise_amt)
print(emp.raise_amt)