class Employee:
    pass


emp = Employee()

# isinstance(obj, class)
print(isinstance(emp, Employee))                    # >> True

emp.first = "Arsalan"
emp.last = "Sadri"
emp.email = "a.sadri@company.com"

print(emp.first)
print(emp.last)
print(emp.email)


