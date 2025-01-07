# imports

from board import Board
from utils import clearScreen, chooseMode


def game():

    # variables
    players = []

    # setup
    board = Board()
    mode = chooseMode()
    clearScreen()


if __name__ == '__main__':
    clearScreen()
    game()