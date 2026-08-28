# --- Exercises: Day 3 ---

# 1. Declare your age as integer variable
age = 20

# 2. Declare your height as a float variable
height = 6.2

# 3. Declare a variable that store a complex number
complex_number = 4 + 1j

# 4. Prompt user to enter base and height of a triangle and calculate area
base = float(input("Enter base: "))
h = float(input("Enter height: ")) # Changed variable name slightly to avoid conflict with 'height' above
area_of_triangle = 0.5 * base * h
print("The area of triangle is ", area_of_triangle)

# 5. Prompt user to enter side a, b, and c and calculate perimeter
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
perimeter_of_triangle = a + b + c
print("The perimeter of the triangle is ", perimeter_of_triangle)

# 6. Get length and width of a rectangle to calculate area and perimeter
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area_of_rectangle = length * width
perimeter_of_rectangle = 2 * (length + width) # Fixed: Perimeter is 2 * (length + width)
print("The area of the rectangle is ", area_of_rectangle)
print("The perimeter of the rectangle is", perimeter_of_rectangle)

# 7. Get radius of a circle and calculate area and circumference
radius = float(input("Enter radius: "))
area_of_circle = 3.14 * radius * radius
circum_of_circle = 2 * 3.14 * radius
print("The area of the circle is ", area_of_circle)
print("The circumference of the circle is", circum_of_circle)

# 8. Calculate the slope, x-intercept and y-intercept of y = 2x - 2
m = 2
c = -2
y_intercept = (m * 0) + c
x_intercept = -c / m
print(f"8. Slope: {m}, Y-Intercept: {y_intercept}, X-Intercept: {x_intercept}")

# 9. Find the slope and Euclidean distance between point (2, 2) and point (6, 10)
x1, y1, x2, y2 = 2, 2, 6, 10
slope_m2 = (y2 - y1) / (x2 - x1)
distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
print(f"9. Slope (m2): {slope_m2}, Euclidean Distance: {distance}")

# 10. Compare the slopes in tasks 8 and 9
m1 = m
print("10. Are the slopes equal?", m1 == slope_m2)

# 11. Calculate the value of y (y = x^2 + 6x + 9) and find when y is 0
# Testing x = -3
x_test = -3
y_value = x_test**2 + 6*x_test + 9
print(f"11. When x is {x_test}, y is {y_value}")

# 12. Find the length of 'python' and 'dragon' and make a falsy comparison statement
print("12. Is length of python not equal to dragon?", len("python") != len("dragon"))

# 13. Use 'and' operator to check if 'on' is found in both 'python' and 'dragon'
both_contain_on = 'on' in 'python' and 'on' in 'dragon'
print("13. Is 'on' in both?", both_contain_on)

# 14. Use 'in' operator to check if 'jargon' is in the sentence
sentence = "I hope this course is not full of jargon"
print("14. Is 'jargon' in sentence?", 'jargon' in sentence)

# 15. There is no 'on' in both dragon and python
print("15. No 'on' in both?", not ('on' in 'python' and 'on' in 'dragon'))

# 16. Find length of 'python', convert to float and then to string
string_length = str(float(len('python')))
print("16. Length as string:", string_length)

# 17. Check if a number is even
number = 10
print("17. Is 10 even?", number % 2 == 0)

# 18. Check if floor division of 7 by 3 is equal to int(2.7)
print("18. Floor division match?", 7 // 3 == int(2.7))

# 19. Check if type of '10' is equal to type of 10
print("19. Type check match?", type('10') == type(10))

# 20. Check if int('9.8') is equal to 10 (Note: needs float conversion first)
# print("20. int('9.8') == 10?", int(float('9.8')) == 10)

# 21. Prompt user for hours and rate to calculate pay
hours = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))
print("21. Your weekly earning is", hours * rate)

# 22. Prompt user for years to calculate seconds lived
years_lived = int(input("Enter number of years you have lived: "))
total_seconds = years_lived * 365 * 24 * 60 * 60
print(f"22. You have lived for {total_seconds} seconds.")

# 23. Display the numeric table
print("23. Table:")
print("1 1 1 1 1\n2 1 2 4 8\n3 1 3 9 27\n4 1 4 16 64\n5 1 5 25 125")