#Create an empty dictionary called dog
dog = {}

#Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Buddy'
dog['color'] = 'Brown'
dog['breed'] = 'Golden Retriever'
dog['legs'] = 4
dog['age'] = 5

#Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {"first_name": "Abdulaziz", "last_name": "Alkhlaiwe", "gender": "Male", "age": 21, "marital status": "not married", "skills": ["Python", "Django"], "country": "KSA", "city": "Riyadh", "address": "east of Riyadh"}
print(student)

#Get the length of the student dictionary
student_length = len(student)
print("Length of student dictionary:", student_length)

#Get the value of skills and check the data type, it should be a list
skills = student.get("skills", [])
print("Skills:", skills)
print("Data type of skills:", type(skills))

#Modify the skills values by adding one or two skills
student["skills"].extend(["JavaScript", "React"])
print("Updated skills:", student["skills"])

#Get the dictionary keys as a list
student_keys = list(student.keys())
print("Student dictionary keys:", student_keys)

#Get the dictionary values as a list
student_values = list(student.values())
print("Student dictionary values:", student_values)

#Change the dictionary to a list of tuples using items() method
student_items = list(student.items())
print("Student dictionary items:", student_items)

#Delete one of the items in the dictionary
del student['marital status']

#Delete one of the dictionaries
del dog
