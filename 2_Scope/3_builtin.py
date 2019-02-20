# BUILT-IN SCOPE
    # Refers to the names that are pre-assigned by Python like built-in functions
    # This include all function, object, variable names 

########## To see all built-ins
import builtins

# print(dir(builtins))

########## 1
    # For example, the min function has a built-in scope
m = min([4 ,5 ,10, -12]) 
print(m)


########## 2
    # Order 
def min():
    pass

min()
