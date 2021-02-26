"""

Me permet de regarder les coordonnés
"""
import pygame
pygame.font.init()
while True:
    pygame.display.set_mode((1080, 720))
    for event in pygame.event.get():
        """
        DEBUGG
        Connaitre la position c'est un plus..
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())

        """Ferme le prgm en cas de fermeture de la fenetre."""
        if event.type == pygame.QUIT:
            running = False