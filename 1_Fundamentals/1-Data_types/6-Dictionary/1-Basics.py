# The notion of key-value pairs
# key is an unique identifier to find a value
# and value is our data 
# It is exactly the same concept and syntax as objects in JS

# Modeling a student as a dictionary
student = {
    "first_name" : "John",
    "last_name" : "Doe",
    "age" : 23,
    "courses": ["Math", "History", "CompSci"]
}

print(type(student))                                # >> <class 'dict'>
print(student)

# Accessing values 
# Via bracket notation
print(student["first_name"])                        # >> John

# Accessing values
# Via .get() method
print(student.get("last_name"))                     # >> Doe
print(student.get("middle_name"))                   # >> None

# Setting a default value for keys that do not exist
print(student.get("middle_name", "default_middle_name"))

# Adding a new pair and/or updating a current pair
# Via bracket notation
student["middle_name"] = "Martin"
student["age"] = 45
print(student)

# Adding a new pair and/or updating a current pair
# Via .update() method
student.update({
    "first_name" : "Sarah",
    "phone" : 2222342245
})
print(student)

# Deleting a pair
# Via del operator 
del student["middle_name"]
print(student)

# via .pop() method
student.pop("age")
print(student)

# Getting the list of all keys
print(student.keys())

# Getting the list of all values
print(student.values())

# Getting all key-value pairs in a set-like format
print(student.items())

# Getting the number of pairs
print(len(student))

# Looping through a dictionary
# Each key gets printed on a separate line 
for key in student: 
    print(key)

# Each pair gets printed on a separate line 
for key, val in student.items(): 
    print(key, val)


