#Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(a,b):
    return a + b
print(add_two_numbers(3, 5))

#Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(r):
    pi = 3.14
    area = pi * r * r
    return area
print(area_of_circle(5))

#Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*args):
    sum = 0
    for i in args:
        if type(i) == int or type(i) == float:
            sum += i
        else:
            return "All items must be numbers"
    return sum

print(add_all_nums(1, 2, 3, 4, 5))

#Temperature in °C can be converted to °F using this formula: °F = (°C x 9 / 5) + 32. Write a function which converts °C to °F, convert_celsius_to - fahrenheit.
def convert_celsius_to_fahrenheit(c):
    f = (c * 9/5) + 32
    return f
print(convert_celsius_to_fahrenheit(0))

#Write a function called check - season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    month = month.lower()
    if month in ['september', 'october', 'november']:
        return "Autumn"
    elif month in ['december', 'january', 'february']:
        return "Winter"
    elif month in ['march', 'april', 'may']:
        return "Spring"
    elif month in ['june', 'july', 'august']:
        return "Summer"
    else:
        return "Invalid month"
print(check_season("March"))

#Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return "Undefined slope"
    return (y2 - y1) / (x2 - x1)

#Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn(a, b, c):
    d = b**2 - 4*a*c
    if d < 0:
        return "No real solution"
    elif d == 0:
        x = -b / (2*a)
        return x
    else:
        x1 = (-b + d**0.5) / (2*a)
        x2 = (-b - d**0.5) / (2*a)
        return x1, x2
print(solve_quadratic_eqn(1, -3, 2))  # (2.0, 1.0)

#Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(lst):
    for item in lst:
        print(item)

"""
Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
print(reverse_list([1, 2, 3, 4, 5]))
[5, 4, 3, 2, 1]

print(reverse_list1(["A", "B", "C"]))
# ["C", "B", "A"]
"""


def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst)-1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst

#Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(lst):
    capitalized_lst = []
    for item in lst:
        capitalized_lst.append(item.upper())
    return capitalized_lst

"""
Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))  # ['Potato', 'Tomato', 'Mango', 'Milk','Meat']
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))      [2, 3, 7, 9, 5]
"""
def add_item(lst, item):
    lst.append(item)
    return lst


"""Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]
"""

def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

"""
Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10))  # 55
print(sum_of_numbers(100))  # 5050
"""

def sum_of_numbers(n):
    return sum(range(n + 1))


#Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.

#Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.


"""
Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
    print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51.
"""


#Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

#Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(param):
    if not param:
        return True
    else:
        return False

#Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
def calculate_mean(lst):
    return sum(lst) / len(lst)
def calculate_median(lst):
    sorted_lst = sorted(lst)
    n = len(lst)
    mid = n // 2
    if n % 2 == 0:
        median = (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        median = sorted_lst[mid]
    return median
def calculate_mode(lst):
    frequency = {}
    for item in lst:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    mode = max(frequency, key=frequency.get)
    return mode
def calculate_range(lst):
    return max(lst) - min(lst)
def calculate_variance(lst):
    mean = calculate_mean(lst)
    variance = sum((x - mean) ** 2 for x in lst) / len(lst)
    return variance
def calculate_std(lst):
    variance = calculate_variance(lst)
    std = variance ** 0.5
    return std

#Write a function called is_prime, which checks if a number is prime.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

#Write a functions which checks if all items are unique in the list.
def all_items_unique(lst):
    return len(lst) == len(set(lst))

#Write a function which checks if all the items of the list are of the same data type.
def all_items_same_type(lst):
    if not lst:
        return True
    first_type = type(lst[0])
    return all(isinstance(item, first_type) for item in lst)

#Write a function which check if provided variable is a valid python variable
def is_valid_variable_name(var_name):
    if not var_name.isidentifier():
        return False
    reserved_keywords = {
        "False", "None", "True", "and", "as", "assert", "async", "await",
        "break", "class", "continue", "def", "del", "elif", "else", "except",
        "finally", "for", "from", "global", "if", "import", "in", "is", "lambda",
        "nonlocal", "not", "or", "pass", "raise", "return", "try", "while", "with",
        "yield"
    }
    return var_name not in reserved_keywords

"""Go to the data folder and access the countries - data.py file.
Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
"""
def most_spoken_languages():
    from countries_data import countries_data
    language_count = {}
    for country in countries_data:
        for language in country['languages']:
            if language in language_count:
                language_count[language] += 1
            else:
                language_count[language] = 1
    sorted_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_languages[:10]
print(most_spoken_languages())
    
def most_populated_countries():
    from countries_data import countries_data
    sorted_countries = sorted(countries_data, key=lambda x: x['population'], reverse=True)
    return [(country['name'], country['population']) for country in sorted_countries[:10]]
print(most_populated_countries())