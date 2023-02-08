from classes.character import Character

class Ninja(Character):
    def __init__( self, name, strength, speed, health ):
        super().__init__(name, strength, speed, health)