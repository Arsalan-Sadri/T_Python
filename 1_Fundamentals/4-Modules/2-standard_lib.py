# "RADNOM" MODULE
import random

# 1
courses = ["History", "Math", "CompSci", "Psychology"]
random_course = random.choice(courses)
print(random_course)                                    # >> History


# "MATH" MODULE
import math

# 1
print(math.sqrt(16))                                    # >> 4.0
print(math.sqrt(9))                                     # >> 3.0


# "DATATIME" MODULE
import datetime

# 1
today = datetime.date.today()
print(today)                                            # >> 2019-01-25


# "CALENDAR" MODULE
import calendar

# 1
print(calendar.isleap(2017))                            # >> False
print(calendar.isleap(2020))                            # >> True


# "OS" MODULE
import os

# 1
pwd = os.getcwd()
print(pwd)

# 2
# Getting the absolute path to the location of a module, which is a .py file 
location = os.__file__
print(location)


