# A class variable is a variable that is shared between
# all instances of that class. In other words, a value 
# that is the same between all instances and is accessed as usuall via
# self keyword. This makes it possible to alter a class variable
# for any instance without affecting the global value.
# To change a class variable, just use <class_name>.<class_variable>. This will
# alter all future instances and already created instances
# If class variable is accessed via an instance of that class, it in fact
# creates/alters an attribute of the same name exclusive to that instance.


class Employee: 

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def full_name(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee("Arsalan", "Sadri", 60000)
emp_2 = Employee("John", "Doe", 50000)

print(emp_1.__dict__)
print(emp_2.__dict__)

emp_1.raise_amount = 1.05
emp_1.apply_raise()
print(emp_1.pay)
print(emp_1.__dict__)

Employee.raise_amount = 1.08
emp_2.apply_raise()
print(emp_2.pay)
print(emp_2.__dict__)

print(emp_1.raise_amount, emp_2.raise_amount)
