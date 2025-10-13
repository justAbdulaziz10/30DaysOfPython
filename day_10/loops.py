# Iterate 0 to 10 using for loop, do the same using while loop.
for i in range(10):
    print(i)
    
print("-----------------------------------------------------------------------------------")

i = 0
while i < 11:
    print(i)
    i += 1

print("-----------------------------------------------------------------------------------")
# Iterate 10 to 0 using for loop, do the same using while loop.
for i in range(10, -1, -1):
    print(i)

print("-----------------------------------------------------------------------------------")

i = 10
while i >= 0:
    print(i)
    i -= 1

print("-----------------------------------------------------------------------------------")

"""
Write a loop that makes seven calls to print(), so we get on the output the following triangle:

  #
  # #
  # ##
  ####
  #####
  ######
  #######
"""

i = 0
while i < 7:
    print('#' * (i + 1))
    i += 1

print("-----------------------------------------------------------------------------------")

"""
Use nested loops to create the following:

# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
"""

"""
Print the following pattern:

0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100
"""

# Iterate through the list, ['Python', 'Numpy', 'Pandas', 'Django', 'Flask'] using a for loop and print out the items.
skils = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for skill in skils:
    print(skill)
    
print("-----------------------------------------------------------------------------------")

# Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(101):
    if i % 2 == 0:
        print(i)

# Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(101):
    if i % 2 == 1:
        print(i)
        
print("-----------------------------------------------------------------------------------")

# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
i = 0
sum = 0
for i in range(101):
    sum += i
print("The sum of all numbers from 0 to 100 is:", sum)
print("-----------------------------------------------------------------------------------")

# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
i = 0
even_sum = 0
odd_sum = 0
for i in range(101):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print("The sum of all even numbers from 0 to 100 is:", even_sum)
print("The sum of all odd numbers from 0 to 100 is:", odd_sum)
print("-----------------------------------------------------------------------------------")

# use the countries.py file. Loop through the countries and extract all the countries containing the word land.
from countries_data import countries_data

for country in countries_data:
    if 'land' in country['name'].lower():
        print(country['name'])
print("-----------------------------------------------------------------------------------")

# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []
for fruit in fruits:
    reversed_fruits.insert(0, fruit)
print(reversed_fruits)
print("-----------------------------------------------------------------------------------")

# What are the total number of languages in the data
total_languages = 0
for country in countries_data:
    total_languages += len(country['languages'])
print("Total number of languages:", total_languages)

# Find the ten most spoken languages from the data
counter = {}
for country in countries_data:
    for language in country['languages']:
        if language in counter:
            counter[language] += 1
        else:
            counter[language] = 1
# Find the top 10 most spoken languages (simple approach without imports or lambdas)
# Convert counter to a list of (language, count) tuples
lang_items = []
for lang in counter:
    lang_items.append((lang, counter[lang]))

# Now find the top 10 by repeated selection (simple selection sort style)
top_languages = []
items_copy = lang_items[:] 
while items_copy and len(top_languages) < 10:
    # find item with max count
    max_item = items_copy[0]
    for it in items_copy:
        if it[1] > max_item[1]:
            max_item = it
    top_languages.append(max_item)
    # remove the selected item
    items_copy.remove(max_item)

print("Top spoken languages (language: count):")
for lang, cnt in top_languages:
    print(f"{lang}: {cnt}")
print("-----------------------------------------------------------------------------------")

# Find the 10 most populated countries in the world (no imports, simple approach)
# Build a list of (country_name, population) tuples. Some entries may not have 'population'; skip those.
pop_list = []
for country in countries_data:
    pop = country.get('population')
    if isinstance(pop, (int, float)):
        pop_list.append((country['name'], pop))

# select top 10 populated countries by repeated selection
top_populated = []
pop_copy = pop_list[:]
while pop_copy and len(top_populated) < 10:
    max_item = pop_copy[0]
    for it in pop_copy:
        if it[1] > max_item[1]:
            max_item = it
    top_populated.append(max_item)
    pop_copy.remove(max_item)

print("Top 10 most populated countries (country: population):")
for name, pop in top_populated:
    print(f"{name}: {pop}")
print("-----------------------------------------------------------------------------------")
