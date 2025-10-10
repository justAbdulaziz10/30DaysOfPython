# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Find the length of the set it_companies
print(len(it_companies))

#Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

#Insert multiple IT companies at once to the set it_companies
it_companies.update(['LinkedIn', 'Snapchat', 'Pinterest'])
print(it_companies)

#Remove one of the companies from the set it_companies
it_companies.remove('Twitter')
print(it_companies)

#What is the difference between remove and discard
# The remove() method will raise an error if the specified item does not exist, while the discard() method will not raise an error.
it_companies.discard('NonExistentCompany')  # This will not raise an error
print(it_companies)

#Join A and B
c = A.union(B)
print(c)

#Find A intersection B
c = A.intersection(B)
print(c)

#Is A subset of B
print(A.issubset(B))

#Are A and B disjoint sets
print(A.isdisjoint(B))

#Join A with B and B with A
c = A.union(B)
print(c)
c = B.union(A)
print(c)

#What is the symmetric difference between A and B
c = A.symmetric_difference(B)
print(c)

#Delete the sets completely
del A
del B
del it_companies

#Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)
print(len(age), len(age_set))

#Explain the difference between the following data types: string, list, tuple and set
#string: An immutable sequence of characters used to represent text.
#list: A mutable ordered collection of items that can contain elements of different data types.
#tuple: An immutable ordered collection of items that can contain elements of different data types.
#set: An unordered collection of unique items.

#I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.split()
unique_words = set(words)
print(len(unique_words))
