from classes.ninja import Ninja
from classes.pirate import Pirate

michelangelo = Ninja("Michelanglo", 10, 5, 50)

jack_sparrow = Pirate("Jack Sparrow", 5, 5, 50)

jack_sparrow.attack(michelangelo)
michelangelo.show_stats()