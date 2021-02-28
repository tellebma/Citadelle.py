import pygame

from Python.network.network import Network
from Python.pygame import setup as f
from Python.conf.settings import Settings


class Multiplayer:
    """
        Classe du mode multijoueur,
        établie la connexion avec le serveur,
        gère toute la partie client serveur.
        cf : server.py
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
        self.host = 0
        self.lobby = False
        self.ingame = False
        self.pseudo = ["Bob", "Toto", "Coucou", "Manges", "Dormir", "Courir", "Maison"]
        self.nb_player = 1
        self.player_id = 1
        self.player_ids = []

        # RESEAU
        self.network = Network()
        self.isIdentifie = False  # esque le client s'est identifié au pres du serveur ?
        # via son id et son pseudo.
        # MENUS
        self.main_menu = main_menu

        # connexion
        self.connexion = self.network.getP()
        print(type(self.connexion))
        print(self.connexion)

    def start(self):
        """
        Fonction qui permet de lancer le multi sur un client.
        """
        print("   _   _              _   _       ")
        print("  / \ / \     _   _  | | | |_  (_)")
        print(" /       \   | | | | | | | __| | |")
        print("/ / \ / \ \  | |_| | | | | |_ || |")
        print("\ /     \ /   \__,_| |_|  \__| |_|")
        if self.verify_connexion():
            print(f"srv :{self.connexion}")
            #self.pseudo = self.connexion[1]
            self.lobby = True
            self.in_lobby()
            self.ingame = True
            self.in_game()
        else:
            pass

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
                                             self.main_menu.screen.get_width() / 2,
                                             self.main_menu.screen.get_height() * 0.20,
                                             (255, 0, 0),
                                             "Arial", 60)
        error_message = f.Center_texte(f"{message}",
                                       self.main_menu.screen.get_width() / 2, self.main_menu.screen.get_height() * 0.30,
                                       (255, 255, 255),
                                       "Arial", 20)
        text, text_rect = error_message_titre.write(self.screen)
        self.screen.blit(text, text_rect)
        text, text_rect = error_message.write(self.screen)
        return text, text_rect

    def verify_connexion(self):
        """
        regarde si la connexion au serveur est possible.
        :return: True Ok , False Nok
        """
        if not self.connexion or self.connexion is None:
            text, text_rect = self.error_message("Connexion avec le serveur non établie ! #E0001")
            self.screen.blit(text, text_rect)
            pygame.display.flip()
            pygame.time.delay(2500)
            self.main_menu.start()
            return False

        else:
            self.connexion = self.connexion.split('|')

            if self.connexion[0] == "Ok":
                """
                Connexion au serveur réussi, vous etes dans la partie.
                """
                self.player_id = self.connexion[1]
                return True
            else:
                print(self.connexion[0])
                print(self.connexion[1])
                text, text_rect = self.error_message(f"Nous avons rencontré une erreur. {self.connexion[1]}")
                self.screen.blit(text, text_rect)
                pygame.display.flip()
                pygame.time.delay(2500)
                self.main_menu.start()
                return False

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

        return self.host

        # def create_button_start(self):
        """

        :return: retourne le boutton. (pour detecter les clicks;)
        """

    #    #return start

    def in_lobby(self):
        """
        Fonction a faire tourner dans le lobby,

        envoie régulièrement des demandes au serveur, sur :

        le nombre de joueur
        TODO Les nom des joueurs
        L'id du joueur, si il est l'host ou non etc.
        à completer.

        :return:
        """
        draw = False
        old_nb_joueurs = 0
        while self.lobby:
            for event in pygame.event.get():
                """Ferme le prgm en cas de fermeture de la fenetre."""
                if event.type == pygame.QUIT:
                    self.main_menu.running = False
                if event.type == pygame.MOUSEBUTTONDOWN and self.host and draw:
                    pos = pygame.mouse.get_pos()
                    if start.click(pos):
                        self.network.send("StartGame")

            if not self.host:
                self.check_if_host()

            player_info = self.network.send("PlayerInfo")
            print(player_info)
            # player info :
            #
            # "PlayerId|nbjoueurconnecte|nbjoueurmax|listJoueurConnecte"
            if player_info == "erreur":
                print(f"erreur lors de la requete PlayerInfo : {player_info}")
            else:
                player_info = player_info.split("|")
                #print("============================")
                #for val in player_info:
                #    print(f"informations recu : {val} | {type(val)}")
                #print("============================")

                self.nb_player = player_info[1]

                nombre_de_joueurs_Max = player_info[2]
                self.player_id = int(player_info[0])
                self.player_ids = player_info[2]

                print(f"Joueurs : {self.nb_player} / {nombre_de_joueurs_Max}")

                if old_nb_joueurs != self.nb_player:
                    draw = False
                    old_nb_joueurs = self.nb_player

                # TODO pseudo
                if not self.isIdentifie:
                    print(self.pseudo[int(self.player_id)])
                    identification = self.network.send(f"Id|{self.pseudo[self.player_id]}")
                    #print(identification)
                    if identification == "Ok":
                        self.isIdentifie = True

                if draw == False:
                    self.screen.fill(0)

                    # PART HOST
                    if self.host:
                        host_message = f.Center_texte("Vous êtes l'hote, c'est vous qui parametrez la partie !",
                                                      self.main_menu.screen.get_width() / 2,
                                                      self.main_menu.screen.get_height() * 0.10,
                                                      (255, 255, 255),
                                                      "Arial", 20)
                        text, text_rect = host_message.write(self.main_menu.screen)
                        self.main_menu.screen.blit(text, text_rect)
                        # On creer le boutton.
                        start = f.Button_center("Start", self.main_menu.screen.get_width() * 0.2,
                                                self.main_menu.screen.get_height() / 2, 150, 100, (0, 255, 0))
                        start.draw(self.main_menu.screen)
                    # Part non host
                    else:
                        host_message = f.Center_texte("Vous êtes connecté, vous attendez que l'hote lance la partie.",
                                                      self.main_menu.screen.get_width() / 2,
                                                      self.main_menu.screen.get_height() * 0.10,
                                                      (255, 255, 255),
                                                      "Arial", 20)
                        text, text_rect = host_message.write(self.main_menu.screen)
                        self.main_menu.screen.blit(text, text_rect)

                    # Texte pour tout le monde:
                    # TODO afficher les noms des jouerus connecté, Host avec étoile  joueur client pseudo en bleu !
                    # affichage du nb de joueur connecté:
                    texte = "Joueurs : " + str(self.nb_player) + " / " + str(nombre_de_joueurs_Max)
                    player_Info_Message = f.Center_texte(texte,
                                                         self.main_menu.screen.get_width() * 0.2,
                                                         self.main_menu.screen.get_height() * 0.2,
                                                         (255, 255, 255),
                                                         "Arial", 15)

                    text, text_rect = player_Info_Message.write(self.screen)
                    self.screen.blit(text, text_rect)

                    # affichage de la liste des joueurs.

                    pygame.display.flip()

                    draw = True

            if self.network.send("IsGameStarted") == "Yes":
                print("lancement de la partie !")
                print(f"Il y a {self.nb_player} joueurs")
                self.lobby = False
                self.inGame = True
                self.in_game()

    def in_game(self):
        draw = False
        while self.ingame:
            if draw == False:
                self.main_menu.screen.fill(0)
                in_Game_Message = f.Center_texte("Vous etes en jeux !! Connaissez vous les règles ?",
                                                 self.main_menu.screen.get_width() * 0.2,
                                                 self.self.main_menu.screen.get_height() * 0.2,
                                                 (255, 255, 255),
                                                 "Arial", 15)
                text, text_rect = in_Game_Message.write(self.main_menu.screen)
                self.main_menu.screen.blit(text, text_rect)
                pygame.display.flip()
            f.pause(1000)

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
