class Character:

    def __init__( self, name, strength, speed, health ):
        self.name = name
        self.strength = strength
        self.speed = speed
        self.health = health

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , opponent ):
        while self.health > 0 and opponent.health > 0:
            opponent.health -= self.strength
            print(f"{self.name} hit {opponent.name} for {self.strength} health points.")

            self.health -= opponent.strength
            print(f"{opponent.name} hit {self.name} for {opponent.strength} health points.")

            if opponent.health <= 0:
                print(f"{opponent.name} died.")
            if self.health <= 0:
                print(f"{self.name} died.")

        return self