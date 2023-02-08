from classes.pets.pet import Pet

class Cat(Pet):
    def __init__(self, name, tricks, sound="Meow"):
        super().__init__(name, tricks, sound)

    def scratch_couch(self):
        print(f"{self.name} scratched the couch!")
        return self