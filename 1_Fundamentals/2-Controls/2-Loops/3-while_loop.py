# WHILE LOOP
# A basic while loop; reapeating for 10 times
x = 0
while x < 10:
    print(x)
    x += 1

# BREAK
# Using break to break out of a while loop 
y = 0
while y < 10:
    if y == 3:
        print("found")
        break
    print(y)
    y += 1

# CONTINUE
# continue can NOT be used in a while loop as 
# there is no iteration established at the beginning so
# the continue command does not know what he next iteration is
z = 0
while z < 10:
    if z == 3:
        print("found")
        continue
    print(z)
    z += 1