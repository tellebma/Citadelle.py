import json
import random

from Python.network.network import Network

from Python.pygame.bank import Bank
from Python.pygame.player import Player

#Lecture du fichier json:
dicts_cartes = {}
with open("cartes.json", "r") as f:
    dicts_cartes = json.load(f)

dicts_cartes_building = dicts_cartes["cards"]["buildings"]
print(dicts_cartes_building)


class Game:

    def __init__(self, game_mode):
        """Initialisation des paramètres de jeu

        Args:
            
            game_mode (Multiplayer ou Solo): [description]
        """
        #SCREEN
        self.screen = game_mode.screen
        self.has_begin = False

        #Serveur
        self.nb_players = game_mode.nb_players
        self.players_id = [i for i in range(1,self.max_player+1)]
        self.max_player = 7
        self.list_player = [Player(self, id) for id in players_id]
        self.network = game_mode.network
        #Banque
        self.bank = Bank()
        #Pioche
        self.pioche = [0]*45

    def mise_en_place(self):
        """
        Mise en place du jeu. 
        Distribution de deux pièces par joueurs
        Distribution de 4 cartes batîments par joueurs
        """
        for player in self.liste_player:
            player.treasure.total_amount = 2 #On distribue 2 pièces par joueur
        self.creation_pioche()

    def creation_pioche(self):
        indices = random.sample(range(1,46),45)
        i=0
        for name_building in dicts_cartes_building.keys():
            quantity = dicts_cartes_building[name_building]["quantity"]
            for n in range(quantity):
                self.pioche[indices[i]-1]=name_building
                i+=1

    def player_draw_ONE_card(self, player):
        pass
    def start(self):
        pass

