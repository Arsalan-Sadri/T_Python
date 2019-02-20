# STATIC METHODS
    # A method that is not dependant to any instance of the class
    # Therefore, they do not take self or cls as their params
    # But, logically connected to the class
    # Like a function which is a part of the class


class Employee: 

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


import datetime
my_date = datetime.date(2018, 1, 29)

print(Employee.is_workday(my_date))




