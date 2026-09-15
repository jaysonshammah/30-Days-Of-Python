# 1. Create an empty dictionary called dog
dog = {}
print("1. Empty dog dictionary:", dog)

# 2. Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Max'
dog['color'] = 'Brown'
dog['breed'] = 'Golden Retriever'
dog['legs'] = 4
dog['age'] = 3
print("2. Dog dictionary:", dog)

student = {
    'first_name':'Omondi',
    'last_name':'Timon',
    'gender':'Male',
    'age': 17,
    'marital_status':'Single',
    'skills': ['Python', 'HTML', 'CSS'],
    'country': 'Kenya',
    'city': 'Nairobi',
    'address': '123 Tech Street'
}

print("3. Student dictionary created.")

# 4. Get the length of the student dictionary
print(len(student))

# 5. Get the value of skills and check the data type
student_skills = student['skills']
print("5. Skills:", student_skills)
print("   Data type of skills:", type(student_skills))

# 6. Modify the skills values by adding one or two skills
student['skills'].append('JavaScript')
student['skills'].extend(['React', 'Git'])
print(student['skills'])

# 7. Get the dictionary keys as a list
student_keys = list(student.keys())
print("7. Student dictionary keys:", student_keys)

# 8. Get the dictionary values as a list
student_values = list(student.values())
print("8. Student dictionary values:", student_values)

print(student.items())

# 10. Delete one of the items in the dictionary
del student['marital_status']
# Alternatively, you could use: student.pop('marital_status')
print("10. Student dictionary after deleting marital_status:\n   ", student.keys())

# 11. Delete one of the dictionaries completely
del dog
print("11. The 'dog' dictionary has been completely deleted.")