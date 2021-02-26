



class Game:
    def __init__(self):
        self.start = False
        self.nb_player = 0
        self.max_player = 7
        self.list_player = []

    def connect(self,idPlayer):
        self.list_player.append(idPlayer)

    def connected(self):
        return self.nb_player