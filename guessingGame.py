'''
ASCII Guessing Game
Milo
'''

import random

def print_treasure_map():
    ''' Prints an ASCCII treasure map. '''
    print(
        '''
        _____
       |     |
       |     |
       |  X  |   ---> Treasure
       |     |
       |     |
        -----
        '''
    )

def play_game():
    print("Welcome to the ASCCII Treasure Hunt!")
    print_treasure_map()
    print("The treasure is hidden behind a number between 1 and 100")

    treasure_number = random.randint(1, 100)
    attempts = 7 # Limit the number of attempts

    while attempts > 0:
        print(f"\nYou have {attempts} attempts remaining.")

        attempts = 0

if __name__ == "__main__":
    play_game()