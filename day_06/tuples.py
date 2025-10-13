#Create an empty tuple
empty_tuple= ()
print(empty_tuple)

#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ()
sisters = ('Joree', 'Hala', 'Farah')
siblings = brothers + sisters
print(brothers)
print(sisters)
print(siblings)

#How many siblings do you have?
print(len(siblings))

#Modify the siblings tuple and add the name of your father and mother and assign it to family_members
father = 'Mohammed'
mother = 'Monerah'
family_members = siblings + (father, mother)
print(family_members)
print(len(family_members))

#Unpack siblings and parents from family_members
sis1, sis2, sis3, dad, mom = family_members
print(sis1)
print(sis2)
print(sis3)
print(dad)
print(mom)

#Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('apple', 'banana', 'cherry')
vegetables = ('carrot', 'broccoli', 'spinach')
animal_products = ('meat', 'milk', 'eggs')
food_stuff_tp = fruits + vegetables + animal_products

#Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

#Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_index = len(food_stuff_tp) // 2
if len(food_stuff_tp) % 2 == 0:
    middle_items = food_stuff_tp[middle_index - 1:middle_index + 1]
else:
    middle_items = food_stuff_tp[middle_index:middle_index + 1]
print(middle_items)

#Slice out the first three items and the last three items from food_staff_lt list
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print(first_three)
print(last_three)

#Delete the food_staff_tp tuple completely
food_stuff_tp = None
print(food_stuff_tp)

"""
Check if 'Estonia' is a nordic country
Check if 'Iceland' is a nordic country

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
"""
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
