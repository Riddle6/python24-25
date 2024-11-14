print("Example 1: \n\n")

# Program will check if a number is even or odd
number = 7

if number % 2 == 0:
    print(number , "is Even.")
else:
    print(number , "is Odd.")


print("\n\nExample 2: \n\n")

# Program will check if a person is eligible to vote
age = 17

if age >= 18:
    print("Yes the can vote.")
else:
    print("Denied. They cannot vote.")


print("\n\nExample 3: \n")

# Program to check if login credentials are correct
username = input("Enter your username: ") # "admin"
password =  input("Enter your password ") # "password123"

if username == "admin" and password == "password123":
    print("Access Granted: Please Proceed")
else:
    print("Unauthorized Access Detected!")

print("\n\nExample 4: \n")

grade = int(input("Please enter Eva's grade for the test: "))

if grade >= 90:
    print("Eva got an A on the Test")
elif grade >= 80:
    print("Eva got a B on the Test")
elif grade >= 70:
    print("Eva got a C on the Test")
elif grade >= 60:
    print("Eva got a D on the Test")
else:
    print("Eva got an F on the Test")