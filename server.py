import socket
from _thread import *
import pickle

# local = 192.168.1.27
# server = 193.168.147.3
server = "localhost"
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


def threaded_client(conn, idJoueur, ishost):
    global nbjconnecte
    global hostPlayerId
    global host
    global nbjmax
    global can_connect_server
    global running_lobby
    global running_game
    running_lobby = True
    running_game = False
    while running_lobby:
        try:
            data = conn.recv(4096).decode()
            if not data:
                break
            else:
                if data == "PlayerInfo":
                    conn.send(str.encode(str(idJoueur) + "|" + str(nbjconnecte) + "|" + str(nbjmax)))

                elif data == "StartGame":
                    conn.send(str.encode("GameStarted"))
                    running_lobby = False
                    can_connect_server = False
                    running_game = True

                elif data == "IsGameStarted":
                    conn.send(str.encode(str("No")))
                else:
                    conn.send(str.encode(str("erreur")))



        except:
            print("Connexion perdu.")
            running_lobby = False
            break
    if running_game:
        print("Game start")
    while running_game:

        try:
            data = conn.recv(4096).decode()
            if not data:
                break
            else:
                if data == "PlayerInfo":
                    conn.send(str.encode(str(idJoueur) + "|" + str(nbjconnecte) + "|" + str(nbjmax)+"|"+str(IdJoueurUtilise)))
                elif data == "IsGameStarted":
                    conn.send(str.encode(str("Yes")))
                    print("Yes, game is live!!")
                else:
                    conn.send(str.encode(str("erreur")))
        except:
            break
        """
        cas d'une déco.
        """

        if running_lobby == False and running_game == False:
            print("Lost connection")
            IdJoueurUtilise.remove(idJoueur)
            nbjconnecte -= 1
            if hostPlayerId == idJoueur:
                if nbjconnecte > 0:
                    hostPlayerId = IdJoueurUtilise[0]
                else:
                    host = False

            # del game[idgame]

            conn.close()
            break


IdJoueurUtilise = []
global nbjconnecte
global host
global hostPlayerId
can_connect_server = True
nbjconnecte = 0
nbjmax = 7
host = False
while True:
    conn, addr = s.accept()
    # print("Connected to:", addr)
    if can_connect_server:

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
            # print("Id Joueur = " + str(IdJoueur))

            nbjconnecte += 1

            if host == False:
                ishost = 1
                host = True
                hostPlayerId = IdJoueur
            else:
                ishost = 0
                # Etat | player n°| isHost ?
        conn.send(str.encode(str("Ok|Player" + str(IdJoueur) + "|" + str(ishost))))
        start_new_thread(threaded_client, (conn, IdJoueur, ishost))
        # print(IdJoueurUtilise)
    else:
        conn.send(str.encode(str("Error|Game Already Started")))
        # error
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
