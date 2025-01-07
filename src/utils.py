# imports

from os import system
from platform import system as systemCheck


# clears the screen
def clearScreen():
    if systemCheck() == 'Windows':
        system('cls')
    else:
        system('clear')

# fuction to choose mode (vs player or computer)
def chooseMode() -> str:
    modes = ['P', 'C']

    while True:
        mode = input('Player(P) or Computer(C): ')
        if mode.upper() in modes:
            return mode.upper()
        else:
            print('Invalid choice. Please enter P or C.')