print("\n######################################")
print("###                                ###")
print("###      Stage of Life Program     ###")
print("###                                ###")
print("###                                ###")
print("###--------------------------------###")
print("###                                ###")
print("###           Questions            ###")
print("###                                ###")
print("vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv\n\n")



name = input("What is your name? ").capitalize()
age = int(input("What is your age? "))

print("Hello " + str(name))

print("\n######################################")
print("###                                ###")
print("###             Results            ###")
print("###                                ###")
print("vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv\n\n")



if age > 7 and age < 13:
    print("You are currently in the childhood stage of your life.")
elif age >= 13 and age < 20:
    print("You are currently in the teenager stage of your life.")
elif age >= 20 and age < 30:
    print("You are currently in the young adult stage of your life.")
elif age >= 30 and age < 56:
    print("You are currently in the adult stage of your life.")
elif age >= 56 and age < 66:
    print("You are currently in a wise stage of your life.")
elif age > 65 and age <= 100:
    print("You are currently in the retirement stage of your life.")
else:
    print("No age group assigned. Age is beyond expectations or is too young.")

