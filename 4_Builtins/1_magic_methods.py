# MAGIC METHODS
    # Are methods of a class, whether built-in or user-defined classes,
    # that get called behind the scene when working with 
    # instances of those clasess. In other words, they are not called directly. 
    # That is, they are not called via <obj_name>.<method_name>. They
    # might get called:
        # <obj_name>
            # print(emp)
        # <class_name>.<method_name>
            # given below
        # <function_name(<obj_name>)>
            # given below
    
    # In case of user-defined classes, these methods can be overwritten
    # to implement what you want to happen when they are called


# 1
    # int.__add__(param)
print(1 + 2)
print(type(1))                                      # >> <class 'int'>
print(int.__add__(1, 2))

print()


# 2
    # str.__add__(param)
print("Hello " + "world!")
print(type("Hello"))                                # >> <class 'str'>
print(str.__add__("Hello ", "world!"))


# 3
    # str.__len__(param)
print(len("test"))                                  # >> 4
print("test".__len__())                             # >> 4