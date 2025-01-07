# imports

from utils import clearScreen


class Board:
    def __init__(self):
        self.board = [['-' for _ in range(7)] for _ in range(6)]
        self.column_count = [0] * 7
        self.last_move = []


    # clears the screen and prints the board.
    def printBoard(self) -> None:
        clearScreen()

        for row in self.board:
            print('[{}]'.format(', '.join(row)))