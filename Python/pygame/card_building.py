import pygame

from cards import Cards

global PATH_BUILDING_CARD = "assets/cartes/buildings/eng/"
global EXTENSION = ".PNG"

class CardBuilding(Cards):

    def __init__(self, building_name):
        super.__init()
        self.path_building = PATH_PERSO_CARD + building_name + EXTENSION
        self.image = pygame.image.load(self.path_building)

        