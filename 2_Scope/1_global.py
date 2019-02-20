# GLOBAL SCOPE
    # Defined globally to the scope of the module or 
    # with the global keyword 

##################### 1
y = "global y"

def f_1():
    print(y)

f_1()                                   # >> global y
print(y)                                # >> global y