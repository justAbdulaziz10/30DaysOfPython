from networkx.algorithms.distance_measures import radius

# Declare your age as integer variable
age = 21

# Declare your height as a float variable
height = 170 #cm

# Declare a variable that store a complex number
exampleOfComplexNumber = 3+4j*7**2/5

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
triangle_base = input("Hello, enter base: ")
triangle_height = input("now enter height: ")
area = 0.5 * triangle_base * triangle_height
print("The area of the triangle is: ", area)

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a = input("Enter side a: ")
side_b = input("Enter side b: ")
side_c = input("Enter side c: ")
perimeter = side_a + side_b + side_c
print("The perimeter of the triangle is: ", perimeter)

# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
rectangle_length = input("Enter length of rectangle: ")
rectangle_width = input("Enter width of rectangle: ")
area_of_rectangle = rectangle_length * rectangle_width
perimeter_of_rectangle = 2 * (rectangle_length + rectangle_width)
print("The area of the rectangle is: ", area_of_rectangle)
print("The perimeter of the rectangle is: ", perimeter_of_rectangle)

# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius = input("Enter radius of circle: ")
pi = 3.14
area_of_circle = pi * radius * radius
circumference = 2 * pi * radius
print("The area of the circle is: ", area_of_circle)
print("The circumference of the circle is: ", circumference)

# Calculate the slope, x-intercept and y-intercept of y = 2x -2
# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1, y1 = 2, 2
x2, y2 = 6, 10
slope = (y2 - y1) / (x2 - x1)
euclidean_distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
y_intercept = -2
x_intercept = -y_intercept / slope
print("The slope is: ", slope)
print("The y-intercept is: ", y_intercept)
print("The x-intercept is: ", x_intercept)

# Compare the slopes in tasks 8 and 9.
slope_task_8 = 2
if slope > slope_task_8:
    print("The slope in task 9 is greater than the slope in task 8.")
elif slope < slope_task_8:
    print("The slope in task 9 is less than the slope in task 8.")
else:
    print("The slopes are equal.")
    
# Calculate the value of y (y = x^2 + 6x + 9) without def. Try to use different x values and figure out at what x value y is going to be 0.

x=0
y = x^2 + 6*x + 9
print("When x is ", x, " y is: ", y)
x=-3
y = x^2 + 6*x + 9
print("When x is ", x, " y is: ", y)
x=3
y = x^2 + 6*x + 9
print("When x is ", x, " y is: ", y)
x=-6
y = x^2 + 6*x + 9
print("When x is ", x, " y is: ", y)
x=6
y = x^2 + 6*x + 9
print("When x is ", x, " y is: ", y)

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
len_python = len('python')
len_dragon = len('dragon')
print("Length of 'python': ", len_python)
print("Length of 'dragon': ", len_dragon)
print("Is length of 'python' not equal to length of 'dragon'? ", len_python != len_dragon)

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print("'on' in 'python' and 'on' in 'dragon': ", 'on' in 'python' and 'on' in 'dragon')

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence = "I hope this course is not full of jargon."
print("'jargon' in sentence: ", 'jargon' in sentence)

# Find the length of the text python and convert the value to float and convert it to string
length_of_python = len('python')
length_as_float = float(length_of_python)
length_as_string = str(length_as_float)
print("Length of 'python' as float: ", length_as_float)
print("Length of 'python' as string: ", length_as_string)

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
number = int(input("Enter a number to check if it's even or not: "))
if number % 2 == 0:
    print(number, " is an even number.")
else:
    print(number, " is not an even number.")
    
# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7
floor_division = 7 // 3
int_converted_value = int(2.7)
print("Is floor division of 7 by 3 equal to int converted value of 2.7? ", floor_division == int_converted_value)

# Check if type of '10' is equal to type of 10
print("Is type of '10' equal to type of 10? ", type('10') == type(10))

# Check if int('9.8') is equal to 10
print("Is int('9.8') equal to 10? ", int(float('9.8')) == 10)

# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = float(input("Enter hours: "))
rate_per_hour = float(input("Enter rate per hour: "))
pay = hours * rate_per_hour
print("Your weekly earning is: ", pay)

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = int(input("Enter number of years you have lived: "))
seconds_in_a_year = 365 * 24 * 60 * 60
total_seconds_lived = years * seconds_in_a_year
print("You have lived for ", total_seconds_lived, " seconds.")

"""Write a Python script that displays the following table
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125"""

print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")
