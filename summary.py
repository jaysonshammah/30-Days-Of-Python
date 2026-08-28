# # print(2 + 3)        #addition
# # print(3 -1)         #SUBTRACTION
# # print(2 * 3)        #multiplication
# # print(3 / 2)
# # print(3 ** 2)       # exponential(**)
# # print(3 % 2)        # modulus(%)
# # print(3 // 2)       # Floor division operator(//)

# # # Checking data types
# # print(type(10))          # Int
# # print(type(3.14))        # Float
# # print(type(1 + 3j))      # Complex number
# # print(type('Asabeneh'))  # String
# # print(type([1, 2, 3]))   # List
# # print(type({'name':'Asabeneh'})) # Dictionary
# # print(type({9.8, 3.14, 2.7}))    # Set
# # print(type((9.8, 3.14, 2.7)))    # Tuple

# # #DAY 2

# # # int to float
# # num_int = 10
# # print('num_int',num_int)         # 10
# # num_float = float(num_int)
# # print('num_float:', num_float)   # 10.0

# # # float to int
# # gravity = 9.81
# # print(int(gravity))             # 9

# # # int to str
# # num_int = 10
# # print(num_int)                  # 10
# # num_str = str(num_int)
# # print(num_str)                  # '10'

# # # str to int or float
# # num_str = '10.6'
# # num_float = float(num_str)  # Convert the string to a float first
# # num_int = int(num_float)    # Then convert the float to an integer
# # print('num_int', int(num_str))      # 10
# # print('num_float', float(num_str))  # 10.6
# # num_int = int(num_float)
# # print('num_int', int(num_int))      # 10

# # # str to list
# # first_name = 'Asabeneh'
# # print(first_name)               # 'Asabeneh'
# # first_name_to_list = list(first_name)
# # print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']

# # # Arithmetic Operations in Python
# # # Integers

# # print('Addition: ', 1 + 2)        # 3
# # print('Subtraction: ', 2 - 1)     # 1
# # print('Multiplication: ', 2 * 3)  # 6
# # print ('Division: ', 4 / 2)       # 2.0  Division in Python gives floating number
# # print('Division: ', 6 / 2)        # 3.0         
# # print('Division: ', 7 / 2)        # 3.5
# # print('Division without the remainder: ', 7 // 2)   # 3,  gives without the floating number or without the remaining
# # print ('Division without the remainder: ',7 // 3)   # 2
# # print('Modulus: ', 3 % 2)         # 1, Gives the remainder
# # print('Exponentiation: ', 2 ** 3) # 8 it means 2 * 2 * 2

# # # Floating numbers
# # print('Floating Point Number, PI', 3.14)
# # print('Floating Point Number, gravity', 9.81)

# # # Complex numbers
# # print('Complex number: ', 1 + 1j)
# # print('Multiplying complex numbers: ',(1 + 1j) * (1 - 1j))


# # num_one = 3
# # num_two = 2

# # total = num_one + num_two
# # diff = num_one - num_two
# # product = num_one * num_two
# # div = num_two / num_one
# # remainder = num_two % num_one

# # # Printing values with label
# # print('total: ', total)
# # print('difference: ', diff)
# # print('product: ', product)
# # print('division: ', div)
# # print('remainder: ', remainder)

# # # Calculating area of a circle
# # radius = 10                                 # radius of a circle
# # area_of_circle = 3.14 * radius ** 2         # two * sign means exponent or power
# # print('Area of a circle:', area_of_circle)

# # # Calculating area of a rectangle
# # length = 10
# # width = 20
# # area_of_rectangle = length * width
# # print('Area of rectangle:', area_of_rectangle)

# # # Calculating a weight of an object
# # mass = 75
# # gravity = 9.81
# # weight = mass * gravity
# # print(weight, 'N')                         # Adding unit to the weight

# # # Calculate the density of a liquid
# # mass = 75 # in Kg
# # volume = 0.075 # in cubic meter
# # density = mass / volume # 1000 Kg/m^3
# # print(density, 'Kg/m^3') # Adding unit to the density


# # #COMPARISON OPERATORS
# # print(3 > 2)     # True, because 3 is greater than 2
# # print(3 >= 2)    # True, because 3 is greater than 2
# # print(3 < 2)     # False,  because 3 is greater than 2
# # print(2 < 3)     # True, because 2 is less than 3
# # print(2 <= 3)    # True, because 2 is less than 3
# # print(3 == 2)    # False, because 3 is not equal to 2
# # print(3 != 2)    # True, because 3 is not equal to 2
# # print(len('mango') == len('avocado'))  # False
# # print(len('mango') != len('avocado'))  # True
# # print(len('mango') < len('avocado'))   # True
# # print(len('milk') != len('meat'))      # False
# # print(len('milk') == len('meat'))      # True
# # print(len('tomato') == len('potato'))  # True
# # print(len('python') > len('dragon'))   # False


# # # Comparing something gives either a True or False

# # print('True == True: ', True == True)
# # print('True == False: ', True == False)
# # print('False == False:', False == False)

# # print(3 > 2 and 4 > 3) # True - because both statements are true
# # print(3 > 2 and 4 < 3) # False - because the second statement is false
# # print(3 < 2 and 4 < 3) # False - because both statements are false
# # print('True and True: ', True and True)
# # print(3 > 2 or 4 > 3)  # True - because both statements are true
# # print(3 > 2 or 4 < 3)  # True - because one of the statements is true
# # print(3 < 2 or 4 < 3)  # False - because both statements are false
# # print('True or False:', True or False)
# # print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
# # print(not True)      # False - Negation, the not operator turns true to false
# # print(not False)     # True
# # print(not not True)  # True
# # print(not not False) # False



# #STRINGS
# letter = 'p'        # A string could be a single character or a bunch of texts
# print(letter)       # P
# print(len(letter))  # 1

# greeting = 'Hello, world!'      # String could be made using a single or double quote,"Hello, World!"
# print(greeting)                 # Hello, World!
# print(len(greeting))            # 13

# multiline_string = '''My name is Jay.
# .This is day 3 of python
# Happy coding!'''
# print(multiline_string)

# first_name = 'Asabeneh'
# last_name = 'Yetayeh'
# space = ' '
# full_name = first_name  +  space + last_name
# print(full_name) # Asabeneh Yetayeh
# # Checking the length of a string using len() built-in function
# print(len(first_name))  # 8
# print(len(last_name))   # 7
# print(len(first_name) > len(last_name)) # True
# print(len(full_name)) # 16


# #\n: new line
# #\t: Tab means(8 spaces)
# #\\: Back slash
# #\': Single quote (')
# #\": Double quote (")

# # print('I hope everyone is enjoying the Python Challenge.\nAre you ?')
# # print('Days\tTopics\tExercises')
# # print('Day 1\t5\t5')
# # print('Day 2\t6\t20')
# # print('Day 3\t5\t23')
# # print('Day 4\t1\t35')
# # print('This is a backslash  symbol (\\)') # To write a backslash
# # print('In every programming language it starts with \"Hello, World!\"') # 


# # %s - String (or any object with a string representation, like numbers)
# # %d - Integers
# # %f - Floating point numbers
# # "%.number of digitsf" - Floating point numbers with fixed precision

# # # Strings only
# # first_name = 'Asabeneh'
# # last_name = 'Yetayeh'
# # language = 'Python'
# # formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
# # print(formated_string)

# # # Strings  and numbers
# # radius = 10
# # pi = 3.14
# # area = pi * radius ** 2
# # formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area) # 2 refers the 2 significant digits after the point
# # python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
# # formated_string = 'The following are python libraries:%s' % (python_libraries)
# # print(formated_string)

# # python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
# # formated_string = 'The following are python libraries:%s' % (python_libraries)
# # print(formated_string) # "The following are python libraries:['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']"``

# # first_name = 'Asabeneh'
# # last_name = 'Yetayeh'
# # language = 'Python'
# # formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
# # print(formated_string)
# # a = 4
# # b = 3

# # print('{} + {} = {}'.format(a, b, a + b))
# # print('{} - {} = {}'.format(a, b, a - b))
# # print('{} * {} = {}'.format(a, b, a * b))
# # print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
# # print('{} % {} = {}'.format(a, b, a % b))
# # print('{} // {} = {}'.format(a, b, a // b))
# # print('{} ** {} = {}'.format(a, b, a ** b))


# # # Strings  and numbers
# # radius = 10
# # pi = 3.14
# # area = pi * radius ** 2
# # formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area) # 2 digits after decimal
# # print(formated_string)

# # 1. Ask the user to enter their details
# full_name = input("Enter your full name: ")
# age_input = input("Enter your age: ")
# height_input = input("Enter your height (in meters): ")
# status_input = input("Are you a student? (True/False): ")

# # 2. Convert the inputs into correct data types
# age = int(age_input)
# height = float(height_input)

# # To convert a string to a boolean properly, check if the text matches "true"
# student_status = status_input.lower() == "true"

# # 3. Display the data in the requested format
# print("\n---STUDENT PROFILE---")
# print(f"Name: {full_name}")
# print(f"Age: {age}")
# print(f"Height: {height} meters")
# print(f"Student: {student_status}")

# # 4. Display the data type of each variable
# print("\nDATA TYPES")
# print(type(full_name))
# print(type(age))
# print(type(height))
# print(type(student_status))


letter = 'P'                # A string could be a single character or a bunch of texts
print(letter)               # P
print(len(letter))          # 1
greeting = 'Hello, World!'  # String could be made using a single or double quote,"Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting))        # 13
sentence = "I hope you are enjoying 30 days of Python Challenge"
print(sentence)

multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)

# Another way of doing the same thing
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)

print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line break
print('Days\tTopics\tExercises') # adding tab space or 4 spaces
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
print('This is a backslash  symbol (\\)') # To write a backslash
print('In every programming language it starts with \"Hello, World!\"') # to write a double quote inside a single quote

# output
#I hope every one is enjoying the Python Challenge.
#Are you ?
#Days  Topics  Exercises
#Day 1	5	    5
#Day 2	6	    20
#Day 3	5	    23
#Day 4	1	    35
#In every programming language it starts with "Hello, World!"
#This is a backslash  symbol (\)

# Strings only
first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formated_string)

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area) # 2 refers the 2 significant digits after the point

python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
formated_string = 'The following are python libraries:%s' % (python_libraries)
print(formated_string) # "The following are python libraries:['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']"


first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print(formated_string)
a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

# output
4 + 3 = 7
4 - 3 = 1
4 * 3 = 12
4 / 3 = 1.33
4 % 3 = 1
4 // 3 = 1
4 ** 3 = 64

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area) # 2 digits after decimal
print(formated_string)

language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n

language = 'Python'
first_letter = language[0]
print(first_letter) # P
second_letter = language[1]
print(second_letter) # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n

language = 'Python'
last_letter = language[-1]
print(last_letter) # n
second_last = language[-2]
print(second_last) # o

language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
print(first_three) #Pyt
last_three = language[3:6]
print(last_three) # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon

greeting = 'Hello, World!'
print(greeting[::-1]) # !dlroW ,olleH

language = 'Python'
pto = language[0:6:2] #
print(pto) # Pto


#lists
# syntax
lst = list()
empty_list = list() # this is an empty list, no item in the list
print(len(empty_list)) # 0
# syntax
lst = []
empty_list = [] # this is an empty list, no item in the list
print(len(empty_list)) # 0
fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway'] 

# Print the lists and its length
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:',animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Countries:', countries)
print('Number of countries:', len(countries))

#output
#Fruits: ['banana', 'orange', 'mango', 'lemon']
#Number of fruits: 4
#Vegetables: ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
#Number of vegetables: 5
#Animal products: ['milk', 'meat', 'butter', 'yoghurt']
#Number of animal products: 4
#Web technologies: ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongDB']
#Number of web technologies: 7
#Countries: ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']
#Number of countries: 5

lst = ['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'}] # list containing different data types

fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0] # we are accessing the first item using its index
print(first_fruit)      # banana
second_fruit = fruits[1]
print(second_fruit)     # orange
last_fruit = fruits[3]
print(last_fruit) # lemon
# Last index
last_index = len(fruits) - 1
last_fruit = fruits[last_index]

#Accessing List Items Using Negative Indexing
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[-4]
last_fruit = fruits[-1]
second_last = fruits[-2]
print(first_fruit)      # banana
print(last_fruit)       # lemon
print(second_last)      # mango

#Unpacking List Items
lst = ['item1','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest)           # ['item4', 'item5']
# First Example
fruits = ['banana', 'orange', 'mango', 'lemon','lime','apple']
first_fruit, second_fruit, third_fruit, *rest = fruits 
print(first_fruit)     # banana
print(second_fruit)    # orange
print(third_fruit)     # mango
print(rest)           # ['lemon','lime','apple']
# Second Example about unpacking list
first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)          # 1
print(second)         # 2
print(third)          # 3
print(rest)           # [4,5,6,7,8,9]
print(tenth)          # 10
# Third Example about unpacking list
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr) 
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)

#Slicing Items from a List
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4] # it returns all the fruits
# this will also give the same result as the one above
all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest
orange_and_mango = fruits[1:3] # it does not include the first index
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[::2] # here we used a 3rd argument, step. It will take every 2cnd item - ['banana', 'mango']

fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:] # it returns all the fruits
orange_and_mango = fruits[-3:-1] # it does not include the last index,['orange', 'mango']
orange_mango_lemon = fruits[-3:] # this will give starting from -3 to the end,['orange', 'mango', 'lemon']
reverse_fruits = fruits[::-1] # a negative step will take the list in reverse order,['lemon', 'mango', 'orange', 'banana']

#Modifying Lists
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
print(fruits)       #  ['avocado', 'orange', 'mango', 'lemon']
fruits[1] = 'apple'
print(fruits)       #  ['avocado', 'apple', 'mango', 'lemon']
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)        #  ['avocado', 'apple', 'mango', 'lime']

#Checking Items in a List
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False

#Adding Items to a List
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append('lime')   # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']
print(fruits)

#Inserting Items into a List
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # insert apple between orange and mango
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')   # ['banana', 'orange', 'apple', 'lime', 'mango', 'lemon']
print(fruits)

#Removing Items from a List
fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.remove('banana')
print(fruits)  # ['orange', 'mango', 'lemon', 'banana'] - this method removes the first occurrence of the item in the list
fruits.remove('lemon')
print(fruits)  # ['orange', 'mango', 'banana']

#The pop() method removes the specified index, (or the last item if index is not specified):
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)       # ['banana', 'orange', 'mango']

fruits.pop(0)
print(fruits)       # ['orange', 'mango']

#Clearing List Items
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)       # []

#Copying a List
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)       # ['banana', 'orange', 'mango', 'lemon']

#Joining Lists
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers) # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables ) # ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']

num1 = [0, 1, 2, 3]
num2= [4, 5, 6]
num1.extend(num2)
print('Numbers:', num1) # Numbers: [0, 1, 2, 3, 4, 5, 6]
negative_numbers = [-5,-4,-3,-2,-1]
positive_numbers = [1, 2, 3,4,5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers) # Integers: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits.extend(vegetables)
print('Fruits and vegetables:', fruits ) # Fruits and vegetables: ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']

#Counting Items in a List
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))           # 3

#Finding Index of an Item
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))           # 2, the first occurrence

#Reversing a List
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits) # ['lemon', 'mango', 'orange', 'banana']
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages) # [24, 25, 24, 26, 25, 24, 19, 22]

#Sorting List Items
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits)             # sorted in alphabetical order, ['banana', 'lemon', 'mango', 'orange']
fruits.sort(reverse=True)
print(fruits) # ['orange', 'mango', 'lemon', 'banana']
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages) #  [19, 22, 24, 24, 24, 25, 25, 26]

ages.sort(reverse=True)
print(ages) #  [26, 25, 25, 24, 24, 24, 22, 19]

#Tuples
# syntax
empty_tuple = ()
# or using the tuple constructor
empty_tuple = tuple()
fruits = ('banana', 'orange', 'mango', 'lemon')

#Accessing Tuple Items
fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[0]
second_fruit = fruits[1]
last_index =len(fruits) - 1
last_fruit = fruits[last_index]

fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[-4]
second_fruit = fruits[-3]
last_fruit = fruits[-1]

#Slicing tuples
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[0:4]         # all items
all_items = tpl[0:]         # all items
middle_two_items = tpl[1:3]  # does not include item at index 3

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:4]    # all items
all_fruits= fruits[0:]      # all items
orange_mango = fruits[1:3]  # doesn't include item at index 3
orange_to_the_rest = fruits[1:]

# Syntax
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[-4:]         # all items
middle_two_items = tpl[-3:-1]  # does not include item at index 3 (-1)

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[-4:]    # all items
orange_mango = fruits[-3:-1]  # doesn't include item at index 3
orange_to_the_rest = fruits[-3:]

#Changing Tuples to Lists
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl)

fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)     # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')

fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)     # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')

#Checking an Item in a Tuple
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
'item2' in tpl # True
fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits) # True
print('apple' in fruits) # False
fruits[0] = 'apple' # TypeError: 'tuple' object does not support item assignment

#Joining Tuples
# syntax
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables

#Deleting Tuples - It is not possible to remove a single item in a tuple but it is possible to delete the tuple itself using del.
# syntax
tpl1 = ('item1', 'item2', 'item3')
del tpl1
fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits