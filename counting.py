'''
Program: counting.py
Author: Christian Riddle

'''

print("Using a continue Statement in a Loop")
print("----------------------------------")

currentNumber = 0

while currentNumber < 10:
    currentNumber += 1 # Control Variable
    if currentNumber % 2 == 0:
        continue

    print(currentNumber)