my_str = "this string is A string Data Type!"
print(my_str)

print(my_str.lower())
print(my_str.upper())
print(my_str.capitalize())

# Counts the number of times the sub-string has occurred
print(my_str.count("string"))
print(my_str.count("universe"))

# Replaces the sub-string with the new
# Does not affect the original sub-string
print(my_str.replace("string", "test", 1))
print(my_str)

# Concatination
new_str = "Hello! " + my_str
print(new_str)

# .format() method 
my_str = "{} My name is {}"
my_str = my_str.format("Hello!", "Arsalan")
print(my_str)

# f string
sub_str_1 = "Hello!"
sub_str_2 = "arsalan"
my_str = f"{sub_str_1} My name is {sub_str_2.capitalize()}"
print(my_str)

# split() 
print(my_str.split("!"))

# If the separator is not found in the string, 
# the resulting list will composed of one string element 
print(my_str.split(","))
