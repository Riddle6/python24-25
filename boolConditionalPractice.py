print("\n\n\n")
print("###########################################")
print("##                                       ##")
print("##              Practice 1               ##")
print("##                                       ##")
print("###########################################")
print("\n\n\n")

# Program to check if a number is positive, negative, or zero
number = -3

# Write an if/else (elif) structure to determine the number's positive, negative, zero state
if number < 0:
    print("This number is negative.")
elif number == 0:
    print("This number is Zero State")
else:
    print("This number is positive.")


print("\n\n\n")
print("###########################################")
print("##                                       ##")
print("##              Practice 2               ##")
print("##                                       ##")
print("###########################################")
print("\n\n\n")

# Program to check if a user has admin privileges
user_role = "admin"

# Write your Code Below
if user_role == "admin":
    print("User has admin privileges")
else:
    print("User has no admin privileges")


print("\n\n\n")
print("###########################################")
print("##                                       ##")
print("##              Practice 3               ##")
print("##                                       ##")
print("###########################################")
print("\n\n\n")

# Program to check if a year is a leap year
year = 2024

# Write your Code Below
if year % 4 == 0 and 100 != 0:
    print("This year is a leap year")
else:
    print("This year is not a leap year")

print("\n\n\n")
print("###########################################")
print("##                                       ##")
print("##              Practice 4               ##")
print("##                                       ##")
print("###########################################")
print("\n\n\n")

# Program to classify age into age groups
age = 20

# Write your Code Below
if age >= 20 and age <= 29:
    print("This person is in their 20s")
elif age >= 30 and age <= 39:
    print("This person is in their 30s")
elif age >= 40 and age <= 49:
    print("This person is in their 40s")
elif age >= 50 and age <= 59:
    print("This person is in their 50s")
elif age >= 10 and age <= 19:
    print("This person is in their early teen to early adult life")
else:
    print("This person is 60 or older.")


print("\n\n\n")
print("###########################################")
print("##                                       ##")
print("##              Practice 5               ##")
print("##                                       ##")
print("###########################################")
print("\n\n\n")

# Program to determine discount based on purchase amount
purchase_amount = 57
discount = 1


def calculate_total():
    if purchase_amount >= 100:
        print("You get a 20" + "%" + " discount")
        total = purchase_amount * (discount - 0.15)
        final = "{:.2f}".format(total)
        print("Your total is: ", final)

    elif purchase_amount >= 80 and purchase_amount <= 99:
        print("You get a 15" + "%" + " discount")
        total = purchase_amount * (discount - 0.15)
        final = "{:.2f}".format(total)
        print("Your total is: ", final)

    elif purchase_amount >= 50 and purchase_amount <= 79:
        print("You get a 10" + "%" + " discount")
        total = purchase_amount * (discount - 0.10)
        final = "{:.2f}".format(total)
        print("Your total is: ", final)
    else:
        print("No discount added.")
        print("Your total is: ", purchase_amount)
        
calculate_total()
# Write your code Below

    