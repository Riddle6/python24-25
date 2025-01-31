# Ask the user for 5 numbers and calculates the sum. Remember about the exceptions
try:   
    result = None
    # The result and all nums are default to None if a user decides to input an invalid value
    num1 = None
    num2 = None
    num3 = None
    num4 = None
    num5 = None

    num1 = int(input("Please enter the 1st integer: "))
    result = num1 
    # The result is set to the current input of the user to avoid a "not defined" exception with result variable.

    num2 = int(input("Please enter the 2nd integer: "))
    result = num1 + num2

    num3 = int(input("Please enter the 3rd integer: "))
    result = num1 + num2 + num3

    num4 = int(input("Please enter the 4th integer: "))
    result = num1 + num2 + num3 + num4

    num5 = int(input("Please enter the 5th integer: "))
    result = num1 + num2 + num3 + num4 + num5


    print(f"The result is: {result}")

except ValueError:
    print("\nThat is not an integer, this value has been skipped.\n")

    try:
        if num1 == None: # If the value is None, it will skip the value and only add up all other values.
            num2 = int(input("Please enter the 2nd integer: "))
            result = num2

            num3 = int(input("Please enter the 3rd integer: "))
            result = num2 + num3

            num4 = int(input("Please enter the 4th integer: "))
            result = num2 + num3 + num4

            num5 = int(input("Please enter the 5th integer: "))
            result = num2 + num3 + num4 + num5

            print(f"\nThe result is: {result}")

        elif num2 == None:
            num3 = int(input("Please enter the 3rd integer: "))
            result = num1 + num3

            num4 = int(input("Please enter the 4th integer: "))
            result = num1 + num3 + num4

            num5 = int(input("Please enter the 5th integer: "))
            result = num1 + num3 + num4 + num5

            print(f"\nThe result is: {result}")
            
        elif num3 == None:
            num4 = int(input("Please enter the 4th integer: "))
            result = num1 + num2 + num4

            num5 = int(input("Please enter the 5th integer: "))
            result = num1 + num2 + num4 + num5

            print(f"\nThe result is: {result}")

        elif num4 == None:
            num5 = int(input("Please enter the 5th integer: "))
            result = num1 + num2 + num3 + num5

            print(f"\nThe result is: {result}")

        else: # If the final integer is invalid, this code will give the result otherwise (The value is skipped).
            result = num1 + num2 + num3 + num4
            print(f"The result is: {result}")
    
    except ValueError: # If the user enters an invalid value once more
        print("\nThat wasn't an integer... AGAIN!\n")