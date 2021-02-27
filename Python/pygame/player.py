from Python.pygame.treasure import Treasure
from Python.pygame.cartes_en_main import CartesEnMain

class Player:
    
    def __init__(self, game, id_player):
        super().__init__()
        self.id_player = id_player
        self.treasure = Treasure(self)
        self.cartes_en_main = CartesEnMain(self)