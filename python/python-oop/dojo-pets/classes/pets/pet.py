class Pet:
    def __init__(self, name, tricks, sound):
        self.name = name
        self.tricks = tricks
        self.sound = sound
        self.energy = 0
        self.health = 10

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        return self
    
    def noise(self):
        print(self.sound)
        return self