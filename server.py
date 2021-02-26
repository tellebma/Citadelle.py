import socket
from _thread import *
import pickle
from game import Game


#local = 192.168.1.27
#server = 193.168.147.3
server = "192.168.1.27"
port = 5555

class Server:
    def __init__(self,id,port):
        self.id = id
        self.port = port
        self.hote = self.get_hote(self)

    def get_joueurs(self):
        """
        retourne une liste avec les joueurs

        :return:
        retourne la liste des joueurs.
        """
        return ["Bob"]

    def get_host(self):
        """
        Définit qui est l'hote de la partie.

        :return:
        retourne le premier joueurs de la liste.
        """
        joueurs = self.get_joueurs()
        self.hote = joueurs[0]
        return joueurs[0]


#bind le port
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


def threaded_client(conn, p, gameId):
    global idCount
    conn.send(str.encode(str(p)))

    reply = ""
    while True:
        try:
            data = conn.recv(4096).decode()

            if gameId in games:
                game = games[gameId]

                if not data:
                    break
                else:
                    if data == "reset":
                        game.resetWent()
                    elif data != "get":
                        game.play(p, data)

                    conn.sendall(pickle.dumps(game))
            else:
                break
        except:
            break

    print("Lost connection")
    try:
        del games[gameId]
        print("Closing Game", gameId)
    except:
        pass
    idCount -= 1
    conn.close()


addr_list = []
port_serveur = [5556 , 5557 , 5558]


while True:
    conn, addr = s.accept()
    Newplayer = True
    for addr_existant in addr_list:
        if addr_existant == addr:
            Newplayer = False
    print("Connected to:", addr)
    print(conn)
    print(addr)

    start_new_thread(threaded_client, (conn, Player, server(Server())))



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