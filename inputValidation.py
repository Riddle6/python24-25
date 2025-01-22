# Ask the user for 5 numbers and calculates the sum. Remember about the exceptions
try:   
    result = None

    num1 = int(input("Please enter an integer: "))
    result = num1 
    # The result is set to the current input of the user to avoid a "not defined" exception with result variable.

    num2 = int(input("Please enter an integer: "))
    result = num1 + num2

    num3 = int(input("Please enter an integer: "))
    result = num1 + num2 + num3

    num4 = int(input("Please enter an integer: "))
    result = num1 + num2 + num3 + num4

    num5 = int(input("Please enter an integer: "))
    result = num1 + num2 + num3 + num4 + num5


    print(f"The result is: {result}")
except ValueError:
    print("That is not an integer, this value has been skipped.")
    print(f"The result is: {result}")