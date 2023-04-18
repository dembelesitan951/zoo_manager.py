# zoo_manager.py

class Animal:
    def __init__(self, name, species, diet):
        self.name = name
        self.species = species
        self.diet = diet

class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal):
        self.animals.remove(animal)

    def feed_animals(self):
        for animal in self.animals:
            print(f"Feeding {animal.name} the {animal.species} a {animal.diet} diet")

zoo = Zoo("Central Park Zoo")

lion = Animal("Simba", "Lion", "Meat")
giraffe = Animal("Melman", "Giraffe", "Plant")
hippo = Animal("Gloria", "Hippo", "Plant")

zoo.add_animal(lion)
zoo.add_animal(giraffe)
zoo.add_animal(hippo)

zoo.feed_animals()
