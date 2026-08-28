# 1. Declare an empty list
empty_list = ()
print(len(empty_list))

# 2. Declare a list with more than 5 items
fruits = ['apple','banana','orange','mango','grape','lemon']
print(fruits)

# 3. Find the length of your list
print(len(fruits))

# 4. Get the first item, the middle item and the last item of the list
first_fruit = fruits[0]
middle_fruit = fruits[len(fruits) // 2]
last_fruit = fruits[-1]
print(f"4. First: {first_fruit}, Middle: {middle_fruit}, Last: {last_fruit}")

# 5. Declare a list called mixed_data_types
mixed_data_types = ['Jayson', 21, 1.75, 'Single', 'Nairobi']
print(mixed_data_types)

# 6. Declare it_companies list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM','Oracle','Amazon']
print(it_companies)

# 8. Print the number of companies
print(len(it_companies))

# 9. Print the first, middle and last company
first_company = it_companies[0]
middle_company = it_companies[len(it_companies) // 2]
last_company = it_companies[-1]
print(f'First: {first_company}, Middle: {middle_company}, Last: {last_company}' )

# 10. Print the list after modifying one of the companies
it_companies[0] = 'Meta'
print(it_companies)

# 11. Add an IT company to it_companies
it_companies.append('Samsung')
print(it_companies)

# 12. Insert an IT company in the middle
middle_index = len(it_companies) // 2
it_companies.insert(middle_index, 'Netflix')
print(it_companies)

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[1] = it_companies[1].upper()
print(it_companies)

# 14. Join the it_companies with a string '#;  '
joined_companies = '#; '.join(it_companies)
print(joined_companies)

# 15. Check if a certain company exists
print('Apple' in it_companies)

# 16. Sort the list using sort()
it_companies.sort()
print(it_companies)

# 17. Reverse the list in descending order using reverse()
it_companies.reverse()
print(it_companies)

# 18. Slice out the first 3 companies
print(it_companies[:3])

# 19. Slice out the last 3 companies
print(it_companies[-3:])

# 20. Slice out the middle IT company or companies
mid_idx = len(it_companies) // 2
# Slicing exactly the middle one if odd, or middle two if even length
print(it_companies[mid_idx:mid_idx+1])

# 21. Remove the first IT company
it_companies.pop(0)
print(it_companies)

# 22. Remove the middle IT company
middle_com = len(it_companies) // 2
print(it_companies.pop(middle_com))

# 23. Remove the last IT company
it_companies.pop() # pop() without index removes the last item
print(it_companies)

# 24. Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# 25. Destroy the IT companies list
del it_companies

# 26. Join the following lists
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
joined_tech = front_end + back_end
print("26. Joined tech lists:", joined_tech)


# 27. Copy the joined list, assign to full_stack, insert Python and SQL after Redux
full_stack = joined_tech.copy()
# Redux is at index 4, so we insert after it (index 5)
redux_index = full_stack.index('Redux')
full_stack.insert(redux_index + 1, 'Python')
full_stack.insert(redux_index + 2, 'SQL')
print(full_stack)

# 1. Sort the list and find the min and max age
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

min_age = ages[0]
max_age = ages[-1]
print(f"Sorted ages: {ages}. Min: {min_age}, Max: {max_age}")

# 2. Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)
# Re-sorting to keep it ordered for the median calculation
ages.sort() 
print("Ages after adding min and max again:", ages)

# 3. Find the median age
n = len(ages)
if n % 2 == 0:
    median_age = (ages[n//2 - 1] + ages[n//2]) / 2
else:
    median_age = ages[n//2]
print("L2-3. Median age:", median_age)

# 4. Find the average age
average_age = sum(ages) / len(ages)
print(f"L2-4. Average age: {average_age:.2f}")

# 5. Find the range of the ages
age_range = max_age - min_age
print("L2-5. Range of ages:", age_range)

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]
# 7. Find the middle country(ies)
mid_country_idx = len(countries) // 2
print("L2-7. Middle country:", countries[mid_country_idx])

# 8. Divide the countries list into two equal lists (or one more for the first half)
if len(countries) % 2 == 0:
    first_half = countries[:mid_country_idx]
    second_half = countries[mid_country_idx:]
else:
    first_half = countries[:mid_country_idx + 1]
    second_half = countries[mid_country_idx + 1:]
    
print(f"L2-8. First half: {first_half}\n      Second half: {second_half}")

# 9. Unpack the first three countries and the rest as scandic countries
country_1, country_2, country_3, *scandic = countries
print(f"L2-9. Unpacked:\n      C1: {country_1}\n      C2: {country_2}\n      C3: {country_3}\n      Scandic: {scandic}")

