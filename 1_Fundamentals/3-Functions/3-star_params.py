# STARRED PARAMETER
    # In case of an unknown/arbitrary number of parameters passed into a function,
    # we can prefix the parameter with * for positional parameters and with ** 
    # for keyword arguments to denote any number of arguments 
    # The star positional arguments is passed to the function as a "tuple" and 
    # the star keyword arguments is passed as a "dictionary" data type.
    # The number (and values) of arguments get determined upon
    # the actual function being called

# 1
    # Conventional names
    # Positional always precedes keyword
def f(*args, **kwargs):
        print(type(args))                   # >> <class 'tuple'>
        print(type(kwargs))                 # >> <class 'dict'>
        print(args)                         # >> (1, 2, 3)
        print(kwargs)                       # >> {'x': 10, 'y': 20}

f(1, 2, 3, x=10, y=20)


# 2
def sum_1(*nums):
    print(type(nums))                       # >> <class 'tuple'>
    print(nums)                             # >> (1, 2, 1, 3)
    
    sum = 0
    for num in nums:
        sum += num
    return sum

print(sum_1(1, 2, 1, 3))                    # >>f 7


# 3
def sum_2(**nums):
        print(type(nums))
        print(nums)
        for num in nums:
            print(num)

sum_2(x=10, y=20)


# 4
    # Star parameters have to be always the last parameter
def quotient(divisor, *nums):
    dividend = 0
    for num in nums:
        dividend += num  
    return dividend // divisor

print(quotient(2, 3, 1, 1, 15))             # >> 10

