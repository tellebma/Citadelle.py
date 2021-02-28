import pygame
import json
import random

if __name__ == "__main__":
    from cards import Cards
else:
    from Python.pygame.cards import Cards

# Lecture du fichier json:
dicts_cartes = {}
with open("../../cartes.json", "r") as f:
    dicts_cartes = json.load(f)

dicts_cartes_building = dicts_cartes["cards"]["buildings"]
# print(dicts_cartes_building)
pioche = [0] * 45

indices = random.sample(range(1, 46), 45)

i = 0
compteur = 0
for name_building in dicts_cartes_building.keys():
    quantity = dicts_cartes_building[name_building]["quantity"]
    print(quantity)
    compteur += quantity

    for n in range(quantity):
        pioche[indices[i] - 1] = name_building
        i += 1
print(pioche)
print(compteur)


class CardBuilding(Cards):

    def __init__(self, building_name):
        super().__init__()
        self.path_building = dicts_cartes_building[building_name][image]
        self.image = pygame.image.load(self.path_building)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
