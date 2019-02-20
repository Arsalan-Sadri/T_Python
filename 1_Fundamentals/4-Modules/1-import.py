# TIPS
    # Files gets imported as an object. 
    # All functions, classes, variables, and objects 
    # in that file are considered to be members of that class and
    # they are all imported automatically and are accessed via 
    # <module_name>.<member_name>
    # Any of these members may also get imported individulally   
    # Modules names cannot begin with numbers 

# HOW TO IMPORT
    # 1
        # import <module_name>
    # 2
        # import <module_name> as <new_name>
    # 3
        # from <module_name> import <function_name>, <variable_name>
    # 4
        # from <module_name> import <function_name> as <new_name>, 
        #                           <variable_name> as <new_name>
    # 5
        # from <module_name> import *
    
# "PATH" LIST
    # Python looks through a path variable, which is a "list" of strings, to find 
    # and import modules. This list is stored in sys.path standard library
    # The first string is absolute path to the current directory

# 1
import sys

print(sys.path)