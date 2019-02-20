# ENCLOSING SCOPE
    # Refers to variables defined in an enclosing fuction

########## 1
def outer():
    x = "outer x"

    def inner():
        x = "inner x"
        print(x)                # >> inner x

    inner()
    print(x)                    # >> outer x


outer() 