# CLASS METHODS AS OBJECT CONSTRUCTORS
    # obj_name = class_name(params)
    # obj_name = class_name.class_method_name(param)



class Employee: 

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)
        


emp_str_1 = "John-Doe-70000"
emp_str_2 = "David-Smith-80000"

# Instantiatioin via the class constructor 
first, last, pay = emp_str_1.split("-")
emp_1 = Employee(first, last, pay)
print(emp_1.first)

# Instantiation via a class method
emp_2 = Employee.from_string(emp_str_2)
print(emp_2.first)



