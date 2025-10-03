# Day 1 - 30DaysOfPython Challenge

print(2 + 3)             # addition(+)
print(3 - 1)             # subtraction(-)
print(2 * 3)             # multiplication(*)
print(3 / 2)             # division(/)
print(3 ** 2)            # exponential(**)
print(3 % 2)             # modulus(%)
print(3 // 2)            # Floor division operator(//)

# Checking data types
print(type(10))          # Int
print(type(3.14))        # Float
print(type(1 + 3j))      # Complex number
print(type('Abdulaziz'))  # String
print(type([1, 2, 3]))   # List
print(type({'name':'Abdulaziz'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple

#Find an Euclidian distance between (2, 3) and (10, 8)
p1 = (2, 3)
p2 = (10, 8)
dis = ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5
print(dis)