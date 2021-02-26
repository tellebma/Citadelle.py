import pygame

from cards import Cards 



class CardPerso(Cards):
    """Création d'une carte personnage. Hérite de la classe Cards
    """
    self.PATH_PERSO_CARD = "assets/cartes/persos/eng/"
    self.EXTENSION = ".PNG"
    def __init__(self, perso_name):
        """Création de la carte demandée

        Args:
            perso_name (str): Le nom du perso: 0n_perso
                                exemple: assassin = 01_assassin
                                         thief = 02_thief
                                        etc...
        """
        super().__init__()
        self.path_perso = self.PATH_PERSO_CARD + perso_name + self.EXTENSION
        self.image = pygame.image.load(self.path_perso)


