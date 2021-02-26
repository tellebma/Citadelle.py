import pygame
from Python.network.network import Network
from Python.conf import settings
from Python.pygame import setup as f
from Python.network import network as n

"""
Affichage :
    Menu de chargement 
    
    
Process:
    Verifier les fichiers du jeu
    Download fichié Maj / reinstall si check sum =/= d'habitude? 
    Chargement des paramètres de jeu.
    
"""


def loading():
    # Check intégrité jeu (ac)
    # Download parties du jeu online
    #
    # Si premiere connexion, enregistré pseudo.
    #
    #
    reglages = settings.Settings()
    global window_width
    window_width = reglages.get_window_width()
    global window_height
    window_height = reglages.get_window_height()
    global pseudo
    pseudo = reglages.get_pseudo()
    # Init Pygame
    pygame.font.init()


def reglage():
    screen.fill(0)
    running = True
    while running:
        Fermer = f.Center_texte("Y en a pas !", window_width / 2, window_width * 0.30,
                                (0, 0, 255),
                                "ComicSansMS", 40)
        text, text_rect = Fermer.write(screen)
        btn = f.Button_center("Menu (retour)", window_width / 2, window_height *0.6, 200, 70, (255, 155, 0))
        btn.draw(screen)
        screen.blit(text, text_rect)
        pygame.display.flip()
        for event in pygame.event.get():
            """Ferme le prgm en cas de fermeture de la fenetre."""
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if btn.click(pos):
                    running = False


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
                                           "ComicSansMS", 50)
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
                                "ComicSansMS", 50)
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
                            "ComicSansMS", 50)
    text, text_rect = Fermer.write(screen)
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.delay(1500)


"""
Conception        Mathieu

Gestion Network   Maxime 

"""


def Multijoueurs():
    print("   _   _              _   _       ")
    print("  / \ / \     _   _  | | | |_  (_)")
    print(" /       \   | | | | | | | __| | |")
    print("/ / \ / \ \  | |_| | | | | |_ || |")
    print("\ /     \ /   \__,_| |_|  \__| |_|")

    pygame.display.set_caption("Citadelle | Multijoueurs")
    screen.fill(1)
    pygame.display.flip()
    running = True
    Network = n.Network()
    answer = Network.getP()
    print("result connexion : "+answer)
    while running:
        pygame.time.delay(1000)
        answer = Network.Get()
        print(f"srv :{answer}")




        for event in pygame.event.get():
            """Ferme le prgm en cas de fermeture de la fenetre."""
            if event.type == pygame.QUIT:
                running = False
        """
        Intérogations serveur : quels sont les serveurs disponible :
        """
        """
        if PlayerId == "1":
            host = True
            f.Center_texte("Vous êtes l'hote, c'est vous qui règler les paramètres de la partie !", window_width / 2, window_width * 0.10,
                           (255, 255, 255),
                           "ComicSansMS", 20)
        if changement:
            pygame.display.flip()
        """


"""
 __  _                _   
/ _\| |_  __ _  _ __ | |_ 
\ \ | __|/ _` || '__|| __|
_\ \| |_| (_| || |   | |_ 
\__/ \__|\__,_||_|    \__|
"""
loading()

screen = pygame.display.set_mode((window_width, window_height))
while True:
    main_menu()
