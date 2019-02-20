tup = ("Art", "CompSci", "SocSci", "Philosophy")

print(type(tup)) # >> <class 'tuple'>
print(tup)
print(tup[0]) # >> Art

# tuples are immutable: items cannot be reassigned
# The following code will generate an error:
# tup[0] = "History"
# Therefore, all methods involving mutation of elements
# cannot be used on tuples.