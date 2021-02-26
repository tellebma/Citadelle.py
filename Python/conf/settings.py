import json
import sys


PATH_SETTINGS = "../../Python/conf/settings.json"

class Settings:

    def __init__(self):
        
        self.path = PATH_SETTINGS
        self.settings = {}

    def read_file(self):
        with open(self.path,"r") as f:
            self.settings = json.load(f)

    def modify_file(self):
        with open(self.path, "w") as f:
            json.dump(self.settings,f)

    def get_window_width(self):
        self.read_file()
        return self.settings["window"]["width"]

    def set_window_width(self, width):
        self.read_file()
        self.settings["window"]["width"] = width
        self.modify_file()
    
    def get_window_height(self):
        self.read_file()
        return self.settings["window"]["height"]

    def set_window_height(self, height):
        self.read_file()
        self.settings["window"]["height"] = height
        self.modify_file()

    def get_parametres_partie(self,nbJoueurs):
        self.read_file()
        return self.settings["nbPlayers"][str(nbJoueurs)]

    def get_pseudo(self):
        pseudo = self.settings["pseudo"]
        return pseudo

    def set_pseudo(self,pseudo):
        self.settings["pseudo"] = pseudo
        return True