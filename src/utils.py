# imports

from os import system
from platform import system as systemCheck


# Clears the screen
def clearScreen():
    if systemCheck() == 'Windows':
        system('cls')
    else:
        system('clear')
