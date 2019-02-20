class Employee: 

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay


class Manager(Employee):
    
    def __init__(self, first, last, pay, employees):
        super().__init__(first, last, pay)
        if employees == None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_employees(self):
        for emp in self.employees:
            print(emp.first)



emp_1 = Employee("Sheldon", "Adelson", 600000)
emp_2 = Employee("Donald", "Trump", 400000)
emp_3 = Employee("Jared", "Kushner", 800000)

print(issubclass(Manager, Employee))                # >> True
print(issubclass(Employee, Manager))                # >> False

mgr = Manager("Michael", "Avenatti", 500000,[emp_1, emp_2])
mgr.add_emp(emp_3)
mgr.print_employees()
print()

mgr.remove_emp(emp_2)
mgr.print_employees()