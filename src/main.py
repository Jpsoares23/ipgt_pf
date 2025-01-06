# imports

from board import Board
from utils import clearScreen


def game():
    board = Board()
    board.printBoard()


if __name__ == '__main__':
    clearScreen()
    game()