# Aims to model mathematical set
# Unordered and non-duplicate lists
# Each time print() gets performed, the order in which 
# items appear may differ

my_set = {"History", "Math", "CompSci", "Philosophy"}

print(type(my_set)) # >> <class 'set'>
print(my_set) # >> {'Math', 'History', 'CompSci', 'Philosophy'}

# Creating empty an empty set
fake_set = {} # This is not going to be a set. This will be a dictionary.
print(type(fake_set)) # >> <class 'dict'>

real_set = set()
print(type(real_set)) # >> <class 'set'>

# Removing an element
my_set.remove("Math")
print(my_set) # >> {'History', 'CompSci', 'Philosophy'}

my_set.discard("CompSci")
print(my_set) # >> {'Philosophy', 'History'}

# in operator 
print("CompSci" in my_set) # >> Flase

# Looping through the sets via "for...in" operator
# Similar to "for...in" in JS
for elm in my_set: 
    print(elm) # >> History Philosophy 


