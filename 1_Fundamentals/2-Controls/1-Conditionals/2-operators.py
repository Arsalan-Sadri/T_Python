# Conditional operators 
# ==
# !=
# > >=
# < <=
# is

lang = "English"
num = 87

if lang == "English": 
    print("lang = English")
if num == 87:
    print("num = 87")
if lang != "Math":
    print("lang != Math")
if num > 80:
    print("num > 80")
if lang > "Apple":
    print("lang > Apple")
if "r" < "s":
    print("r < s")
if "A" < "b":
    print("A < b")


# is operator
# is operator will check to see if 2 objects have the same id
# id's can be retrieved via id() function
# that is, if a is b is equivalent to if id(a) == id(b)

list_a = [1, 2, 3] 
list_b = [1, 2, 3]

if list_a == list_b:
    print("list_a = list_b")

if list_a is list_b:
    print("list_a is list_b")

print(id(list_a))
print(id(list_b))