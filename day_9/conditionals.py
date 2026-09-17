# 1. Check driving age
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    missing_years = 18 - age
    # Using a nested inline condition to handle singular 'year' vs plural 'years'
    print(f"You need {missing_years} more {'years' if missing_years > 1 else 'year'} to learn to drive.")

# 2. Compare ages
my_age = 21
your_age = int(input("Enter your age: "))

if my_age > your_age:
    diff = my_age - your_age
    print(f"I am {diff} {'years' if diff > 1 else 'year'} older than you")
elif your_age > my_age:
    diff = your_age - my_age
    print(f"You are {diff} {'years' if diff > 1 else 'year'} older than me")
else:
    print('We are the same age!')

# 3. Compare numbers
a = int(input('Enter number one: '))
b = int(input('Enter number two: '))

if a > b:
    print(f'{a} is greater than {b}')
elif a < b:
    print(f'{a} is less than {b}')
else:
    print(f"{a} is equal to {b}")

# 3. grading
score = int(input("Enter student's score (0-100): "))
if 90 <= score <= 100:
    print('Grade A')
elif 80 <= score <= 89:
    print('Grade B')
elif 70 <= score <= 79:
    print('Grade C')
elif 60 <= score <= 69:
    print('Grade D')
elif 0 <= score <= 59:
    print('Grade F')
else:
    print('Invalid score entered')

# 4. Seasons Check
month = input('Enter Month: ').capitalize()
if month in ['September', 'October', 'November']:
    print("The season is Autumn.")
elif month in ['December', 'January', 'February']:
    print("The season is Winter.")
elif month in ['March', 'April', 'May']:
    print("The season is Spring.")
elif month in ['June', 'July', 'August']:
    print("The season is Summer.")
else:
    print("Invalid month entered.")


#fruits
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input('Enter to check or add fruit: ').lower()

if new_fruit in fruits:
    print("That fruit already exist in the list")
else:
    fruits.append(new_fruit)
    print("Modified fruits list:", fruits)

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# 1. Check if dictionary has skills key and print middle skill
if 'skills' in person:
    skills = person['skills']
    mid_index = len(skills) // 2
    print("Middle skill:", skills[mid_index])

# 2. Check if dictionary has skills key, and if the person has 'Python'
if 'skills' in person:
    has_python = 'Python' in person['skills']
    print("Has Python skill:", has_python)

# 3. Determine Developer Title based on skills
if 'skills' in person:
    skills_set = set(person['skills'])
    
    # Exact match for front end
    if len(skills_set) == 2 and {'JavaScript', 'React'}.issubset(skills_set):
        print("He is a front end developer")
    # Subsets for backend and fullstack
    elif {'Node', 'Python', 'MongoDB'}.issubset(skills_set):
        print("He is a backend developer")
    elif {'React', 'Node', 'MongoDB'}.issubset(skills_set):
        print("He is a fullstack developer")
    else:
        print("unknown title")

# 4. Check marriage and location status
if person.get('is_married') and person.get('country') == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")