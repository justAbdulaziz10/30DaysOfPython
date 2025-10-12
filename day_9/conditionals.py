"""Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive.
"""

age = input("Enter your age: ")
age = int(age)
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    years_remaining = 18 - age
    print(f"You need {years_remaining} more years to learn to drive.")

"""
Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:

Enter your age: 30
You are 5 years older than me.
"""
my_age=21
your_age = input("Enter your age: ")
your_age = int(your_age)

if my_age > your_age:
    age_diff = my_age - your_age
    if age_diff == 1:
        print("You are 1 year younger than me.")
    else:
        print(f"You are {age_diff} years younger than me.")
elif my_age < your_age:
    age_diff = your_age - my_age
    if age_diff == 1:
        print("You are 1 year older than me.")
    else:
        print(f"You are {age_diff} years older than me.")
else:
    print("We are the same age.")

"""
Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

Enter number one: 4
Enter number two: 3
4 is greater than 3
"""
numberOne = input("Enter number one: ")
numberTwo = input("Enter number two: ")
numberOne = int(numberOne)
numberTwo = int(numberTwo)

if numberOne > numberTwo:
    print(f"{numberOne} is greater than {numberTwo}")
elif numberOne < numberTwo:
    print(f"{numberOne} is smaller than {numberTwo}")
else:
    print(f"{numberOne} is equal to {numberTwo}")

"""Write a code which gives grade to students according to theirs scores:

80-100, A
70-89, B
60-69, C
50-59, D
0-49, F
"""
score = input("Enter your score: ")
score = int(score)

if score >= 80 and score <= 100:
    print("Your grade is A")
elif score >= 70 and score <= 89:
    print("Your grade is B")
elif score >= 60 and score <= 69:
    print("Your grade is C")
elif score >= 50 and score <= 59:
    print("Your grade is D")
elif score >= 0 and score <= 49:
    print("Your grade is F")
else:
    print("Invalid score")

#Check if the season is Autumn, \
    #Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. \
        # December, January or February, the season is Winter.\
            # March, April or May, the season is Spring June,\
                # July or August, the season is Summer
                
month = input("Enter month: ")
month = month.lower()
if month in ['september', 'october', 'november']:
    print("The season is Autumn")
elif month in ['december', 'january', 'february']:
    print("The season is Winter")
elif month in ['march', 'april', 'may']:
    print("The season is Spring")
elif month in ['june', 'july', 'august']:
    print("The season is Summer")
else:
    print("Invalid month")

"""
The following list contains some fruits:

fruits = ['banana', 'orange', 'mango', 'lemon']

If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
"""
fruit = input("Enter a fruit: ")
fruit = fruit.lower()
fruits = ['banana', 'orange', 'mango', 'lemon']

if fruit not in fruits:
    fruits.append(fruit)
    print("Fruit added successfully.")
else:
    print("That fruit already exists in the list.")

"""
Here we have a person dictionary. Feel free to modify it!
        person={
    'first_name': 'Abdulaziz',
    'last_name': 'Alkhlaiwe',
    'age': 21,
    'country': 'Saudi Arabia',
    'is_married': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'East Riyadh',
        'zipcode': '12345'
    }
    }
 * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
 * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB,
    print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title')
    - for more accurate results more conditions can be nested!
 * If the person is not married and if he lives in Saudi Arabia, print the information in the following format:
    Abdulaziz Alkhlaiwe lives in Saudi Arabia. He is not married.
"""

person = {
    'first_name': 'Abdulaziz',
    'last_name': 'Alkhlaiwe',
    'age': 21,
    'country': 'Saudi Arabia',
    'is_married': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'East Riyadh',
        'zipcode': '12345'
    }
}

if 'skills' in person:
    skills = person['skills']
    middle_index = len(skills) // 2
    print(f"The middle skill is: {skills[middle_index]}")

    if 'Python' in skills:
        print("The person has Python skill.")
    else:
        print("The person does not have Python skill.")

    if set(['JavaScript', 'React']).issubset(skills) and len(skills) == 2:
        print("He is a front end developer.")
    elif set(['Node', 'Python', 'MongoDB']).issubset(skills):
        print("He is a backend developer.")
    elif set(['React', 'Node', 'MongoDB']).issubset(skills):
        print("He is a fullstack developer.")
    else:
        print("Unknown title.")
if not person['is_married'] and person['country'] == 'Saudi Arabia':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is not married.")