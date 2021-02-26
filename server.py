import socket
from _thread import *
import pickle
from game import Game

# local = 192.168.1.27
# server = 193.168.147.3
server = "193.168.147.3"
port = 5555



# bind le port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Pas de connexion, Server ready !")

connected = set()
games = {}
idCount = 0


def threaded_client(conn, idJoueur, ishost):
    global nbjconnecte
    global host
    running_lobby = True

    while True:

        while running_lobby:
            """
            On envoie les infos sur la partie.
            """


            """
            On recupere les informations de la partie.

            """
            try:
                print(len(IdJoueurUtilise))
                conn.send(str.encode(str(idJoueur) + "|" + str(ishost) + "|" + str(len(IdJoueurUtilise))))
                data = conn.recv(4096).decode()
                if not data:
                    break
                else:
                    print("data = " + str(data))
            except:
                print("Connexion perdu.")
                running_lobby = False


        """
        cas d'une déco.
        """

        if running_lobby == False:
            print("Lost connection")
            IdJoueurUtilise.remove(idJoueur)
            nbjconnecte -= 1
            if hostPlayerId == idJoueur:
                if nbjconnecte>0:
                    hostPlayerId = IdJoueurUtilise[0]
                else:
                    host = False

            try:
                del games[gameId]
                print("Closing Game", gameId)
            except:
                pass

            conn.close()
            break



IdJoueurUtilise = []
global nbjconnecte
global host
global hostPlayerId
nbjconnecte = 0
nbjmax = 7
host = False
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    if nbjconnecte == nbjmax:
        conn.send(str.encode(str("Error|PlayerLimit")))
    else:

        i = 0
        IdJoueur = 0
        while IdJoueur == 0 and i < nbjmax:
            i += 1
            if IdJoueurUtilise.count(i) == 0:
                IdJoueur = i

        IdJoueurUtilise.append(IdJoueur)
        print("Id Joueur = " + str(IdJoueur))

        nbjconnecte += 1

        if host == False:
            ishost = 1
            host = True
            hostPlayerId = IdJoueur
        else:
            ishost = 0

        start_new_thread(threaded_client, (conn, IdJoueur, ishost))
    print(IdJoueurUtilise)
"""
    idCount += 1
    p = 0
    gameId = (idCount - 1)//2
    if idCount % 2 == 1:
        games[gameId] = Game(gameId)
        print("Creating a new game...")
    else:
        games[gameId].ready = True
        p = 1


    start_new_thread(threaded_client, (conn, p, gameId))


"""
