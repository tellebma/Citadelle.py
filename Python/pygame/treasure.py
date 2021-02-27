
class Treasure(Bank):

    def __init__(self, player):
        super().__init__()
        self.owner = player
        self.total_amount = 0