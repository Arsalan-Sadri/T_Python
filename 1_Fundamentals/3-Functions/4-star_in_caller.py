# USING STAR * WHEN CALLING A FUNCTION
    # If we were to pass a collection/sequence/iterable data type as an argument,
    # we can use * in caller to unpack the data set and
    # send each variable as a separate element

# 1
def f_1(*args):
    print(args)                         

nums = (1, 2 ,3)

f_1(nums)                                 # >> ((1, 2, 3),)
f_1(*nums)                                # >> (1, 2, 3)


# 2
def f_2(**kwargs):
    print(kwargs)

student = {
    "name": "John", 
    "age": 33
    }

f_2(**student)                          # >> {'name': 'John', 'age': 22}
