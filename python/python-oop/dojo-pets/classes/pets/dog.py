from classes.pets.pet import Pet

class Dog(Pet):
    def __init__(self, name, tricks, sound="Woof"):
        super().__init__(name, tricks, sound)

    def wag_tail(self):
        print(f"{self.name} is wagging its tail!")
        return self