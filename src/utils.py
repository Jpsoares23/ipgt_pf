# imports

from os import system
from platform import system as systemCheck
from random import randint
from getpass import getpass

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

# create a list with whho is going first and second
def playOrder(players: list) -> list:
    number = randint(1, 100)
    goesFirst = None
    goesSecond = None
    closestDistance = float('inf')

    for player in players:
        while True:
            try:
                guess = int(getpass(f'{player.name}, choose a number between 1 and 100: '))
                while guess < 1 or guess > 100:
                    print('Invalid guess. Please enter a number between 1 and 100.')
                    guess = int(getpass(f'{player.name}, choose a number between 1 and 100: '))
                break
            except ValueError:
                print("Invalid input. Please enter a valid one.")

        player.playerGuess = guess
        diff = abs(guess - number)

        if diff < closestDistance:
            closestDistance = diff
            goesSecond = goesFirst
            goesFirst = player

        elif diff > closestDistance:
            goesSecond = player

        elif diff == closestDistance:
            clearScreen()
            print('There is a tie. Try again.')
            return playOrder(players)

    return [goesFirst, goesSecond]