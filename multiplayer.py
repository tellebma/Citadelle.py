import pygame

from Python.network.network import Network
from Python.pygame import setup as f
from Python.conf.settings import Settings

class Multiplayer:
    """
    print("   _   _              _   _       ")
    print("  / \ / \     _   _  | | | |_  (_)")
    print(" /       \   | | | | | | | __| | |")
    print("/ / \ / \ \  | |_| | | | | |_ || |")
    print("\ /     \ /   \__,_| |_|  \__| |_|")
    """

    def __init__(self, screen, main_menu):

        # SCREEN
        self.settings = Settings()
        pygame.display.set_caption("Citadelle | Multijoueurs")
        self.screen = screen
        self.screen.fill(0)
        self.window_width = self.settings.get_window_width()
        self.window_height = self.settings.get_window_height()
        pygame.display.flip()

        # PARTIE
        self.lobby = True
        self.ingame = False
        # self.pseudo

        # RESEAU
        self.network = Network()

        # MENUS
        self.main_menu = main_menu

        # connexion
        self.connexion = self.network.getP()
        print(type(self.connexion))
        print(self.connexion)

    def start(self):
        self.verify_connexion()
        print(f"srv :{self.connexion}")
        self.pseudo = self.connexion[1]
        if self.check_if_host():
            self.create_button_start()
        self.in_lobby()
        self.in_game()

    def error_message(self, message):
        """
        AFfichage d'un message d'erreur,
        vous retrouverrez sur git une doc avec tous les message d'erreur possible.

        Titre, erreur
        message

        :param message: le message que l'on souhaite afficher.
        :return: text, text_rect
        """
        error_message_titre = f.Center_texte(f"ERREUR",
                                             self.window_width / 2, self.window_width * 0.20,
                                             (255, 0, 0),
                                             "Arial", 60)
        error_message = f.Center_texte(f"{message}",
                                       self.window_width / 2, self.window_width * 0.30,
                                       (255, 255, 255),
                                       "Arial", 20)
        text, text_rect = error_message_titre.write(self.screen)
        self.screen.blit(text, text_rect)
        text, text_rect = error_message.write(self.screen)
        return text, text_rect

    def verify_connexion(self):
        """
        regarde si la connexion au serveur est possible.
        :return: nothing
        """
        if not self.connexion:
            text, text_rect = self.error_message("Connexion avec le serveur non établie ! #E0001")
            self.screen.blit(text, text_rect)
            pygame.display.flip()
            pygame.time.delay(2500)
            self.main_menu.start()
        else:
            self.connexion = self.connexion.split('|')
        if self.connexion[0] == "Ok":
            """
            Connexion au serveur réussi, vous etes dans la partie.
            """
        else:
            print(self.connexion[0])
            print(self.connexion[1])
            self.error_message(f"Nous avons rencontré une erreur. {self.connexion[1]}")
            pygame.time.delay(1500)
            self.main_menu.start()

    def check_if_host(self):
        """
        Regarde si le Joueur est l'host de la partie.
        :return: nothing.
        """
        if self.connexion[2] == "1":
            """
            regarde si l'option 2 de connexion est a True, si oui alors le joueur est l'hote de la partie.
            """
            self.host = True
            host_message = f.Center_texte("Vous êtes l'hote, c'est vous qui parametrez la partie !",
                                          self.window_width / 2, self.window_width * 0.10,
                                          (255, 255, 255),
                                          "Arial", 20)
            text, text_rect = host_message.write(self.screen)
            self.screen.blit(text, text_rect)
        return self.host

    def create_button_start(self):
        """

        :return: retourne le boutton. (pour detecter les clicks;)
        """
        start = f.Button_center("Start", self.window_width * 0.2, self.window_height / 2, 150, 100, (0, 255, 0))
        start.draw(self.screen)
        return start

    def in_lobby(self):
        draw = False
        old_nb_joueurs = 0
        while self.lobby:
            for event in pygame.event.get():
                """Ferme le prgm en cas de fermeture de la fenetre."""
                if event.type == pygame.QUIT:
                    self.main_menu.running = False
                if event.type == pygame.MOUSEBUTTONDOWN and self.host:
                    pos = pygame.mouse.get_pos()
                    if start.click(pos):
                        self.network.send("StartGame")

            if draw == False:
                pygame.display.flip()

            # pseudo
            player_info = self.network.send("PlayerInfo")
            if player_info == "erreur":
                print(player_info)
            else:
                player_info = player_info.split("|")
                nombre_de_joueurs = player_info[1]

                nombre_de_joueurs_Max = player_info[2]

                if old_nb_joueurs != nombre_de_joueurs:
                    if nombre_de_joueurs == 1:
                        texte = "Joueur : " + str(nombre_de_joueurs) + " / " + str(nombre_de_joueurs_Max)
                    else:
                        texte = "Joueurs : " + str(nombre_de_joueurs) + " / " + str(nombre_de_joueurs_Max)
                    player_Info_Message = f.Center_texte("",
                                                         self.window_width * 0.2, self.window_height * 0.2,
                                                         (255, 255, 255),
                                                         "Arial", 15)
                    player_Info_Message.text = texte
                    player_Info_Message.modifier(texte)
                    text, text_rect = player_Info_Message.write(self.screen)

                    self.screen.blit(text, text_rect)
                    draw = False
                old_nb_joueurs = nombre_de_joueurs

            if self.network.send("IsGameStarted") == "Yes":
                print("lancement de la partie !")

                lobby = False
                inGame = True

    def in_game(self):
        while self.ingame:
            self.main_menu.screen.fill(0)
            in_Game_Message = f.Center_texte("",
                                             self.window_width * 0.2, self.window_height * 0.2,
                                             (255, 255, 255),
                                             "Arial", 15)
            in_Game_Message.text = "Vous etes en jeux !! <br> Connaissez vous les règles ?"
            text, text_rect = in_Game_Message.write(self.main_menu.screen)
            self.main_menu.screen.blit(text, text_rect)
            pygame.display.flip()
            """### AFFICHAGE EXPERIMENTAL DES CARTES BATIMENTS
            card_temple = CardBuilding("temple")
            card_church = CardBuilding("church")
            screen.blit(card_temple.image,(0,0))
            screen.blit(card_church.image,(212,0))"""
            """
             __  _                _   
            / _\| |_  __ _  _ __ | |_ 
            \ \ | __|/ _` || '__|| __|
            _\ \| |_| (_| || |   | |_ 
            \__/ \__|\__,_||_|    \__|
            """
