"""
This program tries to retrieve an integer from the user. If the user enters a string rather than an integer, the program handles it by printing an error.
"""
try:
    my_number = int(input("Enter an integer: "))
    print("Your number: " + str(my_number))
except ValueError:
    print("That wasn't an integer you nitwit!")

print("See... that program is still running.")