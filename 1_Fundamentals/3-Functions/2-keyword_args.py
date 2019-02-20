# ARGUMENTS
    # Positional arguments
        # Arguments are passed by position (conventional arguments) 
    # Keyword arguments
        # Named positional arguments, that is, upon calling the fuction
        # the name of the arguments is used in an assignment.
        # When all arguments are keyword arguments, then the order 
        # does not matter anymore.
# ??
    # So, the arguments that come first cannot be keyword arguments?

def sum(x ,y, z):
    return x + y + z

print(sum(10, 20, 30))                              # >> 60
print(sum(x=10, y=20, z=30))                        # >> 60
print(sum(y=20, z=30, x=10))                        # >> 60
print(sum(10, z=30, y=20))                          # >> 60
print(sum(10, 20, z=30))                            # >> 60

