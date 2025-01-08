class Player:
    def __init__(self, name):
        self.name = name
        self._player_guess = None
    
    @property
    def player_guess(self):
        return self._player_guess

    @player_guess.setter
    def player_guess(self, player_guess):
        self._player_guess = player_guess