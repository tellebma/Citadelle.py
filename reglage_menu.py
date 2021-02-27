import pygame
from Python.pygame import setup as f


class ReglageMenu:

    def __init__(self):
        self.la = "la"











    """
    def reglage():
        screen.fill(0)
        running = True
        while running:
            Fermer = f.Center_texte("Y en a pas !", window_width / 2, window_width * 0.30,
                                    (0, 0, 255),
                                    "ARIAL", 40)
            text, text_rect = Fermer.write(screen)
            btn = f.Button_center("Menu (retour)", window_width / 2, window_height * 0.6, 200, 70, (255, 155, 0))
            btn.draw(screen)
            screen.blit(text, text_rect)
            pygame.display.flip()
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if btn.click(pos):
                        running = False
    """