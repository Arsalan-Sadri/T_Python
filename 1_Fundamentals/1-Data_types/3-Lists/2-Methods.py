courses = ["Math", "Physics", "Chemistry", "CompSci"]

# Adding items to the end of the list 
courses.append("History")
print(courses)

# Adding items at a specific location 
courses.insert(1, "Art")
print(courses)

# Extending a list
more_courses = ["Education", "Networks"]
courses.extend(more_courses)
print(courses)

# Removing an element from a list
courses.remove("Chemistry")
print(courses)

# Removing and returning the last element from the list 
print(courses.pop())
print(courses)

# Reversing the order of items in the list
courses.reverse()
print(courses)

# Sorting a list. By default, in alphabetical order
courses.sort()
print(courses)

# Default sort order: ascending (small to big)
nums = [3, 5, 2, 9, 8]
nums.sort()
print(nums)

# Rerversing the default sort order 
nums.sort(reverse=True)
print(nums)

# Getting the index of an element 
print(courses.index("History"))

# str.join(iter)
# Takes an iterable as param and concatenate 
# its items separated by str, hence returning a string 
courses_str = ", ".join(courses)
print(courses_str)