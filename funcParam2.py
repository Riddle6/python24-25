'''
This program will accept 2 inputs from the user and process the data as exponents of one another.
'''
# This function prints the 2 user inputs and then calculates them as exponents of one another and prints them out to the terminal window.
def myFunction(a, b):
    print("\nVariable a is: ", a, ".")
    print("\nVariable b is: ", b, ".")
    exp1 = a ** b
    exp2 = b ** a
    print("\n", a, " to the power of", b, "is: ", exp1)
    print("\n", b, " to the power of", a, "is: ", exp2)

def sum(first, second):
    total = first + second
    print("The total of your data input is:", total)

while True:
    # Ask the user for 2 integers between 1 and 10.
    a = int(input("\nPlease enter a number between 1 and 10: "))
    b = int(input("\nPlease enter a number between 1 and 10: "))

    myFunction(a, b)


    print("\nPart 2 of our Example:\n")

    # Give the user an option to repeat this process as many times as they want.
    # If they want to quit, they type the word 'Quit'
    # Have users input positive integers
    myVar1 = int(input("Please Enter a positive whole number: "))
    myVar2 = int(input("Please Enter a positive whole number: "))

    # Call the sum() function to process the user input
    sum(myVar1, myVar2)

    repeat = input("Do you want to redo these examples? If not, please enter 'Quit' on your keyboard. \nEnter 'Yes' if you want to continue: ").capitalize()
    if repeat == "Quit":
        break
    elif repeat == "Yes":
        continue