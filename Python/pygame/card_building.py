import pygame

if __name__ == "_main_":
    from cards import Cards

    
else: 
    from Python.pygame.cards import Cards



class CardBuilding(Cards):

    

    def __init__(self, building_name):
        super().__init__()
        self.PATH_BUILDING_CARD = "../../assets/cartes/buildings/eng/"
        self.EXTENSION = ".PNG"
        self.path_building = self.PATH_BUILDING_CARD + building_name + self.EXTENSION
        self.image = pygame.image.load(self.path_building)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        

        
