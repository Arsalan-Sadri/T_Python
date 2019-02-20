# LOCAL SCOPE
    # Any variable defined inside a function is scoped local to that function 
    # unless explicitly defined as global variable 

#################### 1
def f_1():
    x = "local x"
    print(x)

f_1()                                   # >> local x
# print(x)                              # >> NameError: name 'x' is not defined


#################### 2
    # mix and match
z = "global z"

def f_2():
    z = "local z"
    print(z)                            # >> local z

f_2()                                   
print(z)                                # >> global z

#################### 3 
    # mix and match
a = "global a"

def f_3():
    global a
    global b
    a = "local a"
    b = "local b"
    print(a)                            # >> local a
    print(b)                            # >> local b

f_3()                                   
print(a)                                # >> local a
print(b)                                # >> local b

#################### 4
    # Needless to mention, a function's argument is scoped locally 
def f_4(c):
    print(c)

f_4("local c")                          # >> local c
# print(c)                              # >> NameError: name 'c' is not defined
