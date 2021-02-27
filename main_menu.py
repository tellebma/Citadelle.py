import pygame

from Python.pygame import setup as f
from solo import Solo 
from multiplayer import Multiplayer
from reglage_menu import ReglageMenu
from Python.conf.settings import Settings


class MainMenu():
    """
    Menu principale du jeu,

        Solo / Multijoueur
        Fermer
        Reglages

    fenetre pygame

    Classe principale du script.
    """
    def __init__(self):

        self.settings = Settings()
        self.window_width = self.settings.get_window_width()
        self.window_height = self.settings.get_window_height()
        self.pseudo = self.settings.get_pseudo()
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        self.screen.fill(0)
        pygame.display.set_caption("Menu")
        self.draw = False
        self.running = True
    
    def loading(self):
        """
        # Check intégrité jeu (ac)
        # Download parties du jeu online
        #
        # Si premiere connexion, enregistré pseudo.
        #
        #

        """

        
        self.window_width = self.settings.get_window_width()
        
        self.window_height = self.settings.get_window_height()
        
        self.pseudo = self.settings.get_pseudo()
        # Init Pygame
        pygame.font.init()

    def start(self):
        """
        Lancer l'ouverture du jeu,
        """
        self.loading()
        while self.running:
            for event in pygame.event.get():
                """Ferme le prgm en cas de fermeture de la fenetre."""
                if event.type == pygame.QUIT:
                    self.running = False
            message_bienvenue = f.Center_texte("Citadelle".upper(), self.window_width / 2, self.window_height * 0.10, (0, 255, 0),
                                            "ARIAL", 50)
            text, text_rect = message_bienvenue.write(self.screen)
            """
            if pseudo == "":
                message = "Entre ton pseudo"
                pseudo = f.TextBoxInput(Pseudo_InputBox)
            else:
                message = pseudo
            """
            pseudo_inputBox = f.makeTextBox(self.window_width / 2, self.window_height * 0.70, 300, 0, "message")
            #f.showTextBox(pseudo_inputBox)
            btns = [f.Button_center("Solo", self.window_width * 0.2, self.window_height / 2, 150, 100, (0, 0, 255)),
                    f.Button_center("Multi", self.window_width * 0.8, self.window_height / 2, 150, 100, (0, 0, 255)),
                    f.Button_center("reglage", self.window_width * 0.9, self.window_height * 0.9, 150, 100, (0, 0, 0)),
                    f.Button_center("FERMER", self.window_width * 0.9, self.window_height * 0.1, 150, 100, (0, 0, 0))]
            if self.draw != True:

                self.screen.blit(text, text_rect)
                for btn in btns:
                    btn.draw(self.screen)

                self.draw = True

            pygame.display.flip()
            for event in pygame.event.get():
                """
                DEBUGG
                Connaitre la position c'est un plus..
                """
                if event.type == pygame.MOUSEMOTION:
                    # print(pygame.mouse.get_pos())
                    pass
                """Ferme le prgm en cas de fermeture de la fenetre."""
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    for btn in btns:
                        if btn.click(pos):
                            self.running = False
                            clique = btn
            
                    if clique.text == "Solo":
                        solo = Solo(self.screen)
                        solo.start()
                    elif clique.text == "Multi":
                        multi = Multiplayer(self.screen, self)
                        multi.start()

                    elif clique.text == "reglage":
                        menu_reglage = ReglageMenu()
                        menu_reglage.start()

                    elif clique.text == "FERMER":
                        self.screen.fill(0)
                        fermer = f.Center_texte("Merci d'avoir joué !", self.window_width / 2, self.window_width * 0.30,
                                                (0, 255, 0),
                                                "ARIAL", 50)
                        text, text_rect = fermer.write(self.screen)
                        self.screen.blit(text, text_rect)
                        pygame.display.flip()
                        pygame.time.delay(1500)
                        pygame.display.quit()
                        quit()
                    pass
