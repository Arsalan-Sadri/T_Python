# If a class method is accessed via an instance, it will have the 
# same effect as if it were called by the class itself



class Employee: 

    raise_amt = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_emps += 1

    def full_name(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amt):
        cls.raise_amt = amt


emp_1 = Employee("Arsalan", "Sadri", 60000)
emp_2 = Employee("John", "Doe", 50000)

print(Employee.raise_amt)                       # >> 1.04
print(emp_1.raise_amt)                          # >> 1.04
print(emp_2.raise_amt)                          # >> 1.04

Employee.set_raise_amt(1.08)                
print(emp_1.raise_amt)                          # >> 1.08
print(emp_2.raise_amt)                          # >> 1.08

emp_1.set_raise_amt(1.07)
print(emp_1.raise_amt)                          # >> 1.07
print(emp_2.raise_amt)                          # >> 1.07
