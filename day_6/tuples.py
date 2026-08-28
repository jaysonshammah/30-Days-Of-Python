# 1. Create an empty tuple
empty_tuple = ()

# 2. Create a tuple containing names of your sisters and your brothers
brothers_names = ('Jayson','Jayden')
sister_names = ('Jenelle',)

# 3. Join brothers and sisters tuples and assign it to siblings
siblings = brothers_names + sister_names
print(siblings)

# 4. How many siblings do you have?
print(len(siblings))

# 5. Modify the siblings tuple and add the name of your father and mother 
# (Note: Tuples are immutable, so we create a new one by joining)
parents = ('Father','Mother')
family_members = siblings + parents
print(family_members)

# 6. Unpack siblings and parents from family_members
father_and_mother = family_members[3:5]
children = family_members[0:3]
print(father_and_mother)
print(children)
# The asterisk (*) grabs all remaining items into a list, leaving the last two for parents
*unpacked_siblings, father, mother = family_members
print("Unpacked Siblings:", unpacked_siblings)
print("Father:", father)
print("Mother:", mother)

# 2. Create fruits, vegetables and animal products tuples and join them
fruits = ('Apple', 'Banana', 'Mango')
vegetables = ('Carrot', 'Spinach', 'Tomato', 'Onion')
animal_products = ('Milk', 'Cheese', 'Eggs')

food_stuff_tp = fruits + vegetables + animal_products
print("Joined food stuff tuple:", food_stuff_tp)

# 3. Change the food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# 4. Slice out the middle item or items from the tuple or list
mid = len(food_stuff_lt) // 2

if len(food_stuff_lt) % 2 == 0:
    middle_items = food_stuff_lt[mid - 1 : mid + 1]
else:
    middle_items = food_stuff_lt[mid]

print('middle item(s):', middle_items)

# 5. Slice out the first three items and the last three items from food_stuff_lt list
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print("L2-5. First three:", first_three)
print("      Last three:", last_three)

# 6. Delete the food_stuff_tp tuple completely
del food_stuff_tp

nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
# Check if 'Estonia' is a nordic country
is_estonia_nordic = 'Estonia' in nordic_countries
print("L2-7a. Is Estonia a nordic country?", is_estonia_nordic)

# Check if 'Iceland' is a nordic country
is_iceland_nordic = 'Iceland' in nordic_countries
print("L2-7b. Is Iceland a nordic country?", is_iceland_nordic)