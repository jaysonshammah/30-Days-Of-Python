# 1. Concatenate 'Thirty', 'Days', 'Of', 'Python'
conc_string = 'Thirty ' + '' + 'Days ' + '' + 'of ' + '' + 'Python'
print(conc_string)

# 2. Concatenate 'Coding', 'For' , 'All'
str1 = 'Coding ' + '' + 'For ' + '' + 'All'
print(str1)

# 3 & 4. Declare variable and print company
company = 'Coding For All'
print(company)

# 5. Print the length of the string
print(len(company))

# 6. Change to uppercase
company_upper = company.upper()
print(company_upper)

# 7. Change to lowercase
company_lower = company.lower()
print(company_lower)

# 8. capitalize(), title(), swapcase()
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9. Cut (slice) out the first word
print(company[7:])

# 10. Check if string contains the word "Coding"
company = 'Coding For All'
print(company.find('Coding') != -1)

# 11. Replace "Coding" to "Python"
print(company.replace('Coding', 'Python'))

# 13. Split the string using space as the separator
company = 'Coding For All'
print(company.split())

# 14. Split the string at the comma
fortune_five = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(fortune_five.split(', '))

# 15. Character at index 0, last
print(company[0])
print(company[-1])

# 16. Last index of the string
last_index = len(company) - 1
print("16.", last_index)

print(company[10]) # It is a space ' '

# 18. Acronym for 'Python For Everyone'
pfe = 'Python For Everyone'
acronym_pfe = ''.join([word[0] for word in pfe.split()])
print(acronym_pfe)

# 19. Acronym for 'Coding For All'
cfa = 'Coding For All'
acronym_cfa = ''.join([word[0]for word in cfa.split()] )
print(acronym_cfa)

# 20. First occurrence of 'C'
print(cfa.index('C'))

# 21. First occurrence of 'F'
print(cfa.index('F'))

# 22. Last occurrence of 'l' in 'Coding For All People'
print(cfa.rfind('l'))

# 23 & 26. First occurrence of the word 'because'
sn1 = 'You cannot end a sentence with because because because is a conjunction'
print(sn1.find('because'))

# 24. Last occurrence of the word 'because'
sn1 = 'You cannot end a sentence with because because because is a conjunction'
print(sn1.rindex('because'))

# 25 & 27. Slice out the phrase 'because because because'
# Starts at 31, and the phrase is 23 characters long (31 + 23 = 54)
sn2 = 'You cannot end a sentence with because because because is a conjunction'
print(sn2[31:54])

# 28. Does it start with a substring 'Coding'?
print(cfa.startswith('Coding'))

# 29. Does it end with a substring 'coding'?
print(cfa.endswith('Coding'))

# 30. Remove the left and right trailing spaces
spaced_string = '   Coding For All      '
print(repr(spaced_string.strip()))

# 31. Which variable returns True for isidentifier()
sen1 = '30DaysOfPython'  
print(sen1.isidentifier())  # False (starts with a number)
sen2 = 'thirty_days_of_python'
print(sen2.isidentifier())  # True

# 32. Join list with a hash with space string
python_lib = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(python_lib))

# 33. New line escape sequence
print("I am enjoying this challenge.\nI just wonder what is next.")

# 34. Tab escape sequence
print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")

# 35. String formatting for area
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {int(area)} meters square.")

# 36. String formatting for math methods
a, b = 8, 6
print(f"36. {a} + {b} = {a + b}")
print(f"    {a} - {b} = {a - b}")
print(f"    {a} * {b} = {a * b}")
print(f"    {a} / {b} = {a / b:.2f}")
print(f"    {a} % {b} = {a % b}")
print(f"    {a} // {b} = {a // b}")
print(f"    {a} ** {b} = {a ** b}")