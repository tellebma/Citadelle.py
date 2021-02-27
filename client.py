import pygame

from Python.network.network import Network
from Python.conf.settings import Settings
from Python.pygame import setup as f

from main_menu import MainMenu

from Python.pygame.card_building import CardBuilding

"""
Affichage :
    Menu de chargement 
    
    
Process:
    Verifier les fichiers du jeu
    Download fichié Maj / reinstall si check sum =/= d'habitude? 
    Chargement des paramètres de jeu.
    
"""


"""def loading():
    # Check intégrité jeu (ac)
    # Download parties du jeu online
    #
    # Si premiere connexion, enregistré pseudo.
    #
    #
    settings = Settings()
    global window_width
    window_width = settings.get_window_width()
    global window_height
    window_height = settings.get_window_height()
    global pseudo
    pseudo = settings.get_pseudo()
    # Init Pygame
    pygame.font.init()"""

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
            """#Ferme le prgm en cas de fermeture de la fenetre.
"""
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if btn.click(pos):
                    running = False

"""
"""
Affichage:
    au milieu bouton de jeu 
        pseudo
        
        Solo
        
        Multi
            
            credit défilant.

process:
    wait
"""


def main_menu():
    screen.fill(0)
    pygame.display.set_caption("Menu")
    draw = 0
    running = True
    while running:
        for event in pygame.event.get():
            """Ferme le prgm en cas de fermeture de la fenetre."""
            if event.type == pygame.QUIT:
                running = False
        Message_Bienvenue = f.Center_texte("Citadelle".upper(), window_width / 2, window_height * 0.10, (0, 255, 0),
                                           "ARIAL", 50)
        text, text_rect = Message_Bienvenue.write(screen)
        """
        if pseudo == "":
            message = "Entre ton pseudo"
            pseudo = f.TextBoxInput(Pseudo_InputBox)
        else:
            message = pseudo
        """
        Pseudo_InputBox = f.makeTextBox(window_width / 2, window_height * 0.70, 300, 0, "message")
        #f.showTextBox(Pseudo_InputBox)
        btns = [f.Button_center("Solo", window_width * 0.2, window_height / 2, 150, 100, (0, 0, 255)),
                f.Button_center("Multi", window_width * 0.8, window_height / 2, 150, 100, (0, 0, 255)),
                f.Button_center("reglage", window_width * 0.9, window_height * 0.9, 150, 100, (0, 0, 0)),
                f.Button_center("FERMER", window_width * 0.9, window_height * 0.1, 150, 100, (0, 0, 0))]
        if draw != True:

            screen.blit(text, text_rect)
            for btn in btns:
                btn.draw(screen)

            draw = True

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
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for btn in btns:
                    if btn.click(pos):
                        running = False
                        clique = btn

    if clique.text == "Solo":
        Solo()
    elif clique.text == "Multi":
        Multijoueurs()
    elif clique.text == "reglage":
        reglage()
    elif clique.text == "FERMER":
        screen.fill(0)
        Fermer = f.Center_texte("Merci d'avoir joué !", window_width / 2, window_width * 0.30,
                                (0, 255, 0),
                                "ARIAL", 50)
        text, text_rect = Fermer.write(screen)
        screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.delay(1500)
        pygame.display.quit()
        quit()
    pass


"""
Gestion Mathieu
"""


def Solo():
    screen.fill(0)
    Fermer = f.Center_texte("Bientôt un Solo !", window_width / 2, window_width * 0.30,
                            (0, 255, 0),
                            "ARIAL", 50)
    text, text_rect = Fermer.write(screen)
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.delay(1500)


"""
Conception        Mathieu

Gestion Network   Maxime 

"""


"""def Multijoueurs():
    
    print("   _   _              _   _       ")
    print("  / \ / \     _   _  | | | |_  (_)")
    print(" /       \   | | | | | | | __| | |")
    print("/ / \ / \ \  | |_| | | | | |_ || |")
    print("\ /     \ /   \__,_| |_|  \__| |_|")
    
    pygame.display.set_caption("Citadelle | Multijoueurs")
    screen.fill(0)
    pygame.display.flip()
    Lobby = True
    Network = n.Network()

    connexion = Network.getP()
    print(type(connexion))
    print(connexion)
    if not connexion :
        error_message_titre = f.Center_texte(f"ERREUR",
                                             window_width / 2, window_width * 0.20,
                                             (255, 0, 0),
                                             "Arial", 60)
        error_message = f.Center_texte(f"Nos serveurs rencontres des erreurs.",
                                       window_width / 2, window_width * 0.30,
                                       (255, 255, 255),
                                       "Arial", 20)
        text, text_rect = error_message_titre.write(screen)
        screen.blit(text, text_rect)
        text, text_rect = error_message.write(screen)
        screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.delay(2500)
        main_menu()
    else:
        connexion = connexion.split('|')
    if connexion[0] == "Ok":
        print("ok")
    else:
        print(connexion[0])
        print(connexion[1])
        error_message = f.Center_texte(f"Nous avons rencontré une erreur. {connexion[1]}",
                                       window_width / 2, window_width * 0.10,
                                       (255, 255, 255),
                                       "Arial", 20)
        text, text_rect = error_message.write(screen)
        screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.delay(1500)
        main_menu()

    print(f"srv :{connexion}")
    pseudo = connexion[1]
    if connexion[2] == "1":
        
        #regarde si l'option 2 de connexion est a True, si oui alors le joueur est l'hote de la partie.
        
        host = True
        host_message = f.Center_texte("Vous êtes l'hote, c'est vous qui règler les paramètres de la partie !",
                                      window_width / 2, window_width * 0.10,
                                      (255, 255, 255),
                                      "Arial", 20)
        text, text_rect = host_message.write(screen)
        screen.blit(text, text_rect)
        start = f.Button_center("Start", window_width * 0.2, window_height / 2, 150, 100, (0, 255, 0))
        start.draw(screen)

    draw = False
    Old_nb_joueurs = 0

    while Lobby:
        for event in pygame.event.get():
            """"""Ferme le prgm en cas de fermeture de la fenetre.""""""
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and host:
                pos = pygame.mouse.get_pos()
                if start.click(pos):
                    Network.send("StartGame")


        if draw == False:
            pygame.display.flip()

        #pseudo
        PlayerInfo = Network.send("PlayerInfo")
        if PlayerInfo == "erreur":
            print(PlayerInfo)
        else:
            PlayerInfo =PlayerInfo.split("|")
            Nombre_de_joueurs = PlayerInfo[1]

            Nombre_de_joueurs_Max = PlayerInfo[2]



            if Old_nb_joueurs != Nombre_de_joueurs:
                if Nombre_de_joueurs == 1:
                    texte = "Joueur : " + str(Nombre_de_joueurs) + " / " + str(Nombre_de_joueurs_Max)
                else:
                    texte = "Joueurs : " + str(Nombre_de_joueurs) + " / " + str(Nombre_de_joueurs_Max)
                Player_Info_Message = f.Center_texte("",
                                                     window_width * 0.2, window_width * 0.2,
                                                     (255, 255, 255),
                                                     "Arial", 15)
                Player_Info_Message.text = texte
                Player_Info_Message.modifier(texte)
                text, text_rect = Player_Info_Message.write(screen)

                screen.blit(text, text_rect)
                draw = False
            Old_nb_joueurs = Nombre_de_joueurs

        if Network.send("IsGameStarted") == "Yes":
            print("lancement de la partie !")

            Lobby = False
            InGame = True
    while InGame:

        screen.fill(0)
        InGameMessage = f.Center_texte("",
                                             window_width * 0.2, window_width * 0.2,
                                             (255, 255, 255),
                                             "Arial", 15)
        InGameMessage.text = "Vous etes en jeux !!\nConnaissez vous les règles ?"
        text, text_rect = Player_Info_Message.write(screen)
        screen.blit(text, text_rect)
        pygame.display.flip()
        ### AFFICHAGE EXPERIMENTAL DES CARTES BATIMENTS
        card_temple = CardBuilding("temple")
        card_church = CardBuilding("church")
        screen.blit(card_temple.image,(0,0))
        screen.blit(card_church.image,(212,0))

 __  _                _   
/ _\| |_  __ _  _ __ | |_ 
\ \ | __|/ _` || '__|| __|
_\ \| |_| (_| || |   | |_ 
\__/ \__|\__,_||_|    \__|
"""



main_menu = MainMenu()
while True:
    #main_menu()
    main_menu.start()

