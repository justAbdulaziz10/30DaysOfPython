#Day 2: 30 Days of python programming

first_name = 'Abdulaziz'
last_name = 'Alkhlaiwe'
full_name = first_name + ' ' + last_name
country = "Saudi Arabia"
city = "Riyadh"
age = 21
year_of_birth = 2004
is_married = False
is_true = True
is_light_on = True


friend_name, friend_age, friend_country = 'Omar', 21, 'KSA'

#Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year_of_birth))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(friend_name))
print(type(friend_age))
print(type(friend_country))

#Using the len() built-in function, find the length of your first name
print(len(first_name))

#Compare the length of your first name and your last name
print(len(first_name) == len(last_name))

#Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

#Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
print(total)

#Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two
print(diff)

#Multiply num_two and num_one and assign the value to a variable product
product = num_one * num_two
print(product)

#Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two
print(division)

#Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one
print(remainder)

#Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
print(exp)

#Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two
print(floor_division)

"""
The radius of a circle is 30 meters.
Calculate the area of a circle and assign the value to a variable name of area_of_circle
Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
Take radius as user input and calculate the area.

"""
area_of_circle = 3.14 * 30 * 30
print(area_of_circle)
circum_of_circle = 2 * 3.14 * 30
print(circum_of_circle)

first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
country = input("What country do you live in? ")
age = input("How old are you? ")
print(f"Your name is {first_name} {last_name}. You live in {country} and you are {age} years old.")
