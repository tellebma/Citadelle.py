
class CartesEnMain(List):

    def __init__(self, player):
        super().__init__()
        self.cartes_en_main = []
        self.owner = player

    def tire_une_carte(self, name_building):
        self.cartes_en_main.append(name_building)

    def joue_une_carte(self, name_building):
        #Supprimer la carte de la main
        self.cartes_en_main.remove(name_building)
    
    def get_cartes_en_main(self):
        return self.cartes_en_main

