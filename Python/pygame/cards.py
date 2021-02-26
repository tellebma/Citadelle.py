import pygame
import json





class Cards(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        #Dimension
        self.width = 270
        self.height = 420
        #Image
        self.image = pygame.image.load("cartes/buildings/eng/_buildings_verso.PNG") #par défaut, retournée
        pygame.transform.scale(self.image, width, height)
        self.rect = image.get_rect()
        self.rect.x = self.rect.x + self.width/2
        self.rect.y = self.rect.y + self.height/2

        

