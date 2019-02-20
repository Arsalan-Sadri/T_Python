set_1 = {"History", "CompSci", "Art"}
set_2 = {"History", "CompSci", "Math", "Physics"}
set_3 = {"History", "CompSci"}

# Find out which items are in common in 2 sets
print(set_1.intersection(set_2)) # >> {'History', 'CompSci'}
print(set_1.intersection(set_2)) # >> {'History', 'CompSci'}

# Find out which items are in set_1 but not in set_2
print(set_1.difference(set_2)) # >> {'Art'}

# Find out which elements are in set_2 but not in set_1
print(set_2.difference(set_1)) # >> {'Math', 'Physics'}

# Find out the union of both sets 
print(set_1.union(set_2)) # >> {'Physics', 'CompSci', 'History', 'Math', 'Art'}

# Find out if a set is a sub set of another set
print(set_1.issubset(set_2)) # >> False
print(set_3.issubset(set_1)) # >> True

# Find out if a set is a super set of another set
print(set_1.issuperset(set_3)) # >> True