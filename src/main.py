# imports

from player import Player
from board import Board
from utils import clearScreen, chooseMode


def game():

    # variables
    players = []

    # setup
    board = Board()
    mode = chooseMode()
    clearScreen()

    # if player vs player mode choosen
    if mode == 'P':
        playerName = [input(f"Enter Player {i + 1}'s name: ") for i in range(2)] # choose players name
        players = [Player(name) for name in playerName] # create player object
        clearScreen()

    else:
        ...


if __name__ == '__main__':
    clearScreen()
    game()