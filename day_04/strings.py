#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
from networkx.algorithms.distance_measures import radius
contained = ''.join(
    ['Thirty', 'Days', 'Of', 'Python']
)

#Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
CFA = ' '.join(['Coding', 'For', 'All'])

#Declare a variable named company and assign it to an initial value "Coding For All".
company = CFA

#Print the variable company using print().
print(company)

#Print the length of the company string using len() method and print().
print(len(company))


#Change all the characters to uppercase letters using upper() method.
print(company.upper())

#Change all the characters to lowercase letters using lower() method.
print(company.lower())


#Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

#Cut(slice) out the first word of Coding For All string.
print(company[7:])

#Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.find("Coding"))
print(company.index("Coding"))

#Replace the word coding in the string 'Coding For All' to Python.
print(company.replace("Coding", "Python"))

#Change Python for Everyone to Python for All using the replace method or other methods.
print(company.replace("Everyone", "All"))

#Split the string 'Coding For All' using space as the separator (split()).
print(company.split(" "))


#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(","))


#What is the character at index 0 in the string Coding For All.
print(company[0])

#What is the last index of the string Coding For All.
print(len(company) - 1)

#What character is at index 10 in "Coding For All" string.
print(company[10])


#Create an acronym or an abbreviation for the name 'Python For Everyone'.
PFE = 'Python For Everyone'
print(PFE[0] + PFE[7] + PFE[11])

#Create an acronym or an abbreviation for the name 'Coding For All'.
CFA = 'Coding For All'
print(CFA[0] + CFA[7] + CFA[11])

#Use index to determine the position of the first occurrence of C in Coding For All.
print(CFA.index("C"))

#Use index to determine the position of the first occurrence of F in Coding For All.
print(CFA.index("F"))

#Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(CFA.rfind("l"))

#Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print("You cannot end a sentence with because because because is a conjunction".find("because"))


#Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print("You cannot end a sentence with because because because is a conjunction".rindex("because"))

#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print("You cannot end a sentence with because because because is a conjunction"[31:60])

#Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print("You cannot end a sentence with because because because is a conjunction".find("because"))

#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print("You cannot end a sentence with because because because is a conjunction"[31:60])

#Does ''Coding For All' start with a substring Coding?
print(company.startswith("Coding"))

#Does 'Coding For All' end with a substring coding?
print(company.endswith("coding"))

#'   Coding For All      '  , remove the left and right trailing spaces in the given string.
print(company.strip())


"""Which one of the following variables return True when we use the method isidentifier():
30DaysOfPython
thirty_days_of_python"""
print("30DaysOfPython".isidentifier()) # False
print("thirty_days_of_python".isidentifier()) # True


#The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
print(' # '.join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))

"""Use the new line escape sequence to separate the following sentences.
I am enjoying this challenge.
I just wonder what is next."""
print("I am enjoying this challenge.\nI just wonder what is next.")

"""Use a tab escape sequence to write the following lines.
Name      Age     Country   City
Asabeneh  250     Finland   Helsinki"""
print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")

"""Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square."""

radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {} meters square.".format(radius, area))


"""
Make the following using string formatting methods:
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
"""

a = 8
b = 6
print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {:.2f}".format(a, b, a / b))
print("{} % {} = {}".format(a, b, a % b))
print("{} // {} = {}".format(a, b, a // b))
print("{} ** {} = {}".format(a, b, a ** b))
