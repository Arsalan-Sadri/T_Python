# # abs() function
# num = -5
# print(num)
# print(abs(num))

# # round() function
# # It rounds it up to the nearest integer 
# num = 4.6
# print(round(num))

# num = 4.4
# print(round(num))

# # Type casting: str to int
# num_1 = "100"
# num_2 = "200"
# print(num_1 + num_2) # >> "100200"

# num_1 = int(num_1)
# num_2 = int(num_2)
# print(num_1 + num_2) # >> 300

# # Type casting: str to float
# num_1 = "100"
# num_2 = "200"

# num_1 = float(num_1)
# num_2 = float(num_2)
# print(num_1 + num_2) # >> 300.0

# num = 43.55
# print(int(num)) # >> 43
# print(float(num)) # >> 43.55

# num = "42.12"
# print(int(num))
# print(float(num)) # >> 42.12

# RANGE() FUNCTION
    # range(start, stop)
    # Creates a sequence from start to stop (not including stop)

# 1
seq = range(1, 5)
for num in seq:
    print(num)

# 2
    # If there is no start parameter, it starts from 0
    # range(n): 0 to n-1
seq = range(6)
for num in seq:
    print(num)
