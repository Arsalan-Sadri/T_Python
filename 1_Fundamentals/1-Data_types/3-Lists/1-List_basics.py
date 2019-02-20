courses = ["Math", "Physics", "Chemistry", "CompSci"]

# The "courses" list automatically becomes 
# an object of "list" class
print(type(courses))
print(courses)

print(len(courses)) # >> 4

# Accessing items
print(courses[1])   # >> Physics

# Accessing a range of items
print(courses[0:2]) # >> ['Math', 'Physics']
print(courses[:2]) # >> ['Math', 'Physics']

print(courses[2:])  # >> ["Chemistry, "CompSci"]

# in operator
print("Physics" in courses)
print("Art" in courses)
