# Properly call the function with the values of 5 and 10

def add_numbers(a, b):
    return a + b

result = add_numbers(5, 10)
#print(f"{result}")


# Complete the code to define a function that calculates area of a circle. The function should take radius as an argument and return the area using the formula pi * radius^2. Assume that pi = 3.14
def calculate_area(radius):
    
    return 3.14 * radius ** 2

area = calculate_area(7)
#print(f"The area is: {area}")


# Complete the function that calculates the product and difference of two numbers. The function should return both values.
def calculate_values(x, y):
    product = x * y
    difference = x - y
    return product, difference

prod, diff = calculate_values(8, 3)
print(f"Product: {prod}")
print(f"Difference: {diff}")