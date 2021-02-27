
class Bank:

    def __init__(self):
        super().__init__()
        self.total_amount = 30

    def retrait(self, retrait):
        if self.total_amount - retrait >=0:
            self.total_amount -= retrait
        else:
            #Afficher un message d'erreur (Vous ne pouvez pas retirer cet argent!)
            pass
    
    def depot(self, depot):
        self.total_amount += depot

    def get_total_amount(self):
        return self.total_amount

    
