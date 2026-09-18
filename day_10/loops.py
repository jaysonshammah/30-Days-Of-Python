# 1. Iterate 0 to 10 using for loop and while loop
print("1a. For loop (0 to 10):")
for i in range(11):
    print(i, end=" ")
print("\n1b. While loop (0 to 10):")
count = 0
while count <= 10:
    print(count, end=" ")
    count += 1
print()

# 2. Iterate 10 to 0 using for loop and while loop
print("\n2a. For loop (10 to 0):")
for i in range(10, -1, -1):
    print(i, end=" ")
print("\n2b. While loop (10 to 0):")
count = 10
while count >= 0:
    print(count, end=" ")
    count -= 1
print()

## 3. Print a triangle of '#'
print("\n3. Triangle pattern:")
for i in range(1,8):
    print('#' * i)

# 4. Use nested loops to create an 8x8 grid
print("\n4. 8x8 Grid:")
for i in range(8):
    for j in range(8):
        print('#', end="")
    print()

# 5. Print the multiplication pattern
print("\n5. Multiplication pattern:")
for i in range(11):
    print(f'{i} X {i} = {i*i}')

# 6. Iterate through a list
print("\n6. Iterate through list:")
tech_list = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for language in tech_list:
    print(language)

# 7. Print only even numbers from 0 to 100
print("\n7. Even numbers (0-10):") 
for i in range(0, 101, 2): 
    print(i, end=" ")
print()

# 8. Print only odd numbers from 0 to 100
print("\n8. Odd numbers (0-10):") 
for i in range(1, 101, 2): 
    print(i, end=" ")
print("\n")

# 1. Print the sum of all numbers from 0 to 100
total_sum = 0
for i in range(101):
    total_sum += i
print(f"L2-1. The sum of all numbers is {total_sum}.")

# 2. Print the sum of all evens and the sum of all odds from 0 to 100
even_sum = 0
odd_sum = 0
for i in range(101):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print(f"L2-2. The sum of all evens is {even_sum}. And the sum of all odds is {odd_sum}.\n")

from data.countries import countries

# Now you can use the 'countries' list just like you wrote it in this file!
print("Total number of countries:", len(countries))

land_countries = []
for country in countries:
    if 'land' in country.lower():
        land_countries.append(country)

print("Countries with 'land' in their name:")
for c in land_countries:
    print(f"- {c}")

# 2. Reverse a fruit list using a loop (without using .reverse())
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []
for i in range(len(fruits) - 1, -1, -1):
    reversed_fruits.append(fruits[i])
print(f"L3-2. Reversed fruits list: {reversed_fruits}")

# 3a. Total number of languages in the data
from data.countries_data import countries_data
all_languages = set()
for country in countries_data:
    for language in country['languages']:
        all_languages.add(language)
print(f"L3-3a. Total number of unique languages: {len(all_languages)}")

# 3b. Find the ten most spoken languages
language_counts = {}
for country in countries_data:
    for language in country['languages']:
        language_counts[language] = language_counts.get(language, 0) + 1

# Sort languages by their frequency (value) in descending order
sorted_languages = sorted(language_counts.items(), key=lambda x: x[1], reverse=True)
print("L3-3b. Most spoken languages (top 10):")
for lang, count in sorted_languages[:10]:
    print(f"       {lang}: {count} countries")

# 3c. Find the 10 most populated countries
# Sort the countries_data list of dictionaries by the 'population' key
sorted_by_population = sorted(countries_data, key=lambda c: c['population'], reverse=True)
print("L3-3c. 10 Most populated countries:")
for country in sorted_by_population[:10]:
    print(f"       {country['name']}: {country['population']:,}")