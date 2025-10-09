# Declare an empty list
list = []

# Declare a list with more than 5 items
list2 = [1, 2, 3, 4, 5, 5]

# Find the length of your list
print(len(list2))

# Get the first item, the middle item and the last item of the list
print("first item is:", list2[0])
print("first item is:", list2[len(list2) // 2])
print("first item is:", list2[-1])

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Abdulaziz", "21", "170cm", "not married", "KSA"]

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# Print the list using print()
print(it_companies)

# Print the number of companies in the list
print(len(it_companies))
# Print the first, middle and last company
print("first company is:", it_companies[0])
print("middle company is:", it_companies[len(it_companies) // 2])
print("last company is:", it_companies[-1])

# Print the list after modifying one of the companies
it_companies[0] = "Mara"
print(it_companies)

# Add an IT company to it_companies
it_companies.append("tesla")
print(it_companies)

# Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies) // 2, "Spotify")
print(it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[1] = it_companies[1].upper()
print(it_companies)

# Join the it_companies with a string '#;  '
joined_compaines = '#: '.join(it_companies)
print(joined_compaines)

# Check if a certain company exists in the it_companies list.
print("Is Amazon exist in the list?", "Amazon" in it_companies)

# Sort the list using sort() method
it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# Slice out the first 3 companies from the list
first_three_companies = it_companies[:3]
print("First three companies are:", first_three_companies)

# Slice out the last 3 companies from the list
last_three_companies = it_companies[-3:]
print("Last three companies are:", last_three_companies)

# Slice out the middle IT company or companies from the list
middle_company = it_companies[len(it_companies) // 2]
print("Middle company is:", middle_company)

# Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)

# Remove the middle IT company or companies from the list
it_companies.pop(len(it_companies) // 2)
print(it_companies)

# Remove the last IT company from the list
it_companies.pop()
print(it_companies)

# Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# Destroy the IT companies list
del it_companies

"""
Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
"""

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
joined_list = front_end + back_end
print(joined_list)

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.

full_stack = joined_list.copy()
full_stack.insert(full_stack.index("Redux") + 1, "Python")
full_stack.insert(full_stack.index("Python") + 1, "SQL")
print(full_stack)

"""The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]"""

# Sort the list and find the min and max age
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
minAge = ages[0]
maxAge = ages[-1]
print("min age is:", minAge)
print("max age is:", maxAge)

# Add the min age and the max age again to the list
ages.append(minAge)
ages.append(maxAge)
print(ages)

# Find the median age (one middle item or two middle items divided by two)
medAge = ages[len(ages) // 2]
print("median age is:", medAge)

# Find the average age (sum of all items divided by their number)
avgAge = sum(ages) / len(ages)
print("average age is:", avgAge)

# Find the range of the ages (max minus min)
rangeAge = maxAge - minAge
print("range of ages is:", rangeAge)

# Compare the value of (min - average) and (max - average), use abs() method
print("abs(min- avg): " , abs(minAge - avgAge))
print("abs(max- avg): " , abs(maxAge - avgAge))

"""
Find the middle country(ies) in the countries list
Divide the countries list into two equal lists if it is even if not one more country for the first half.
['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark'].
"""
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
middle_country = countries[len(countries) // 2]
print("middle country is:", middle_country)
firstList = countries[:len(countries) // 2 + 1]
secondList = countries[len(countries) // 2 + 1:]
print("First list is:", firstList)
print("Second list is:", secondList)

# Unpack the first three countries and the rest as scandic countries.
scandic_countries = countries[:3]
print("Scandic countries are:", scandic_countries)
