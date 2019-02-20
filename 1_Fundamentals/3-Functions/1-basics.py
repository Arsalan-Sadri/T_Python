# FUNCTIONS

# 1 
def hello_func():
    print("Hello world function!")

hello_func()

# 2
def return_hello_func():
    return "Hello is returned!"

print(return_hello_func())

# 3
def sum_func(x, y):
    return x + y

print(sum_func(2, 3))

# 4
def sum_default_func(x, y = 4):
    return x + y

print(sum_default_func(3, 10))
print(sum_default_func(3))