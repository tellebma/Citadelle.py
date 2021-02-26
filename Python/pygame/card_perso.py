import pygame

from cards import Cards 

global PATH_PERSO_CARD = "assets/cartes/persos/eng/"
global EXTENSION = ".PNG"

class CardPerso(Cards):
    """Création d'une carte personnage. Hérite de la classe Cards
    """

    def __init__(self, perso_name):
        """Création de la carte demandée

        Args:
            perso_name (str): Le nom du perso: 0n_perso
                                exemple: assassin = 01_assassin
                                         thief = 02_thief
                                        etc...
        """
        super.__init__()
        self.path_perso = PATH_PERSO_CARD + perso_name + EXTENSION
        self.image = pygame.image.load(self.path_perso)


