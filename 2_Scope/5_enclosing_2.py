# ENCLOSING SCOPE
    # How to access an enclosing variable from inside enclosed function

########## 1
def outer():
    x = "outer x"

    def inner():
        nonlocal x
        x = "inner x"
        print(x)                # >> inner x

    inner()
    print(x)                    # >> inner x


outer() 