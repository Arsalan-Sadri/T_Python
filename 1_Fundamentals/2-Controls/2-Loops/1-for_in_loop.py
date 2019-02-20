# FOR IN
    # To loop through any iterable object/sequence/collection like
    # list, set, tuples, dictionary, or a string

# Looping through a string
for letter in "test":
    print(letter)

# Looping through a list
nums = [1, 2, 3, 4, 5]

for num in nums:
    print(num)

# BREAK
    # always breaks out of a loop AND the closest loop
for num in nums:
    if num == 3:
        print("found!")
        break
    print(num)

# CONTINUE
    # moves to the next iteration 
for num in nums:
    if num == 3:
        print("found!")
        continue    
    print(num)
