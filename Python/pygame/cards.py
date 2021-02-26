import pygame
import json





class Cards(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        #Dimension
        self.width = int(270/2)
        self.height = int(420/2)
        #Image
        self.image = pygame.image.load("../../assets/cartes/buildings/eng/_buildings_verso.PNG") #par défaut, retournée
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.x + self.width/2
        self.rect.y = self.rect.y + self.height/2



