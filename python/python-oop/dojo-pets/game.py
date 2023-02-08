from classes.ninja import Ninja
from classes.pets.dog import Dog
from classes.pets.cat import Cat

pet1 = Dog("Bob", ["Spin", "Roll over", "Play dead"])
ninja1 = Ninja("Reece", "Hunter", "cinnamon roll", "kibble", pet1)

pet2 = Cat("Sally", ["Lay down", "Play dead"])
ninja2 = Ninja("Kyle", "Michaelson", "bacon", "wet food", pet2)

ninja1.walk().feed().bathe()
ninja1.pet.wag_tail()

ninja2.walk().feed().bathe()
ninja2.pet.scratch_couch()