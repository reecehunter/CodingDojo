class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        print(f"Walking {self.pet.name}.")
        self.pet.play()
        return self

    def feed(self):
        print(f"Feeding {self.pet.name} {self.treats}.")
        self.pet.eat()
        return self

    def bathe(self):
        print(f"Bathing {self.pet.name}.")
        self.pet.noise()
        return self