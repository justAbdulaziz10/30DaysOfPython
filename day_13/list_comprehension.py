"""
Filter only negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
"""
print([num for num in [-4, -3, -2, -1, 0, 2, 4, 6] if num <= 0])


"""
Flatten the following list of lists of lists to a one dimensional list:

list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

output
[1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

print([num for sublist1 in [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]] for sublist2 in sublist1 for num in sublist2])


"""
Using list comprehension create the following list of tuples:

[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]
"""

print([(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)])

"""
Flatten the following list to a new list:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output:
[['FINLAND', 'FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
"""

print([[country[0].upper(), country[0][:3].upper(), country[1].upper()] for sublist in [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]] for country in sublist])


"""
Change the following list to a list of dictionaries:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output:
[{'country': 'FINLAND', 'city': 'HELSINKI'},
{'country': 'SWEDEN', 'city': 'STOCKHOLM'},
{'country': 'NORWAY', 'city': 'OSLO'}]
"""
print([{'country': country[0].upper(), 'city': country[1].upper()} for sublist in [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]] for country in sublist])


"""Change the following list of lists to a list of concatenated strings:

names = [[('Abdulaziz', 'Alkhlaiwe')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
output
['Abdulaziz Alkhlaiwe', 'David Smith', 'Donald Trump', 'Bill Gates']
"""
print([f'{name[0]} {name[1]}' for sublist in [[('Abdulaziz', 'Alkhlaiwe')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]] for name in sublist])

#Write a lambda function which can solve a slope or y - intercept of linear functions.

slope_intercept = lambda m, b, x: m * x + b
