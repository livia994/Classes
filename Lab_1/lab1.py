class Animals:
    count = 0

    def __init__(self, name, species, owner_name):
        self.name = name
        self.species = species
        self.owner_name = owner_name
        Animals.count += 1

    def displayCount(self):
        print("Total number of Animals registered at the Vet Clinic: ", Animals.count)

    def displayAnimals(self):
        print("Name of the Animal is: ", self.name)
        print("Species of the Animal: ", self.species)
        print("Owner's name: ", self.owner_name)

if __name__ == "__main__":
    animal_1 = Animals("Mia", "Cat", "Melissa Smith")
    animal_2 = Animals("Max", "Dog", "Tom Ford")
    animal_3 = Animals("Roxy", "Parrot", " Lia Jansen")

    animal_1.displayAnimals()
    animal_2.displayAnimals()
    animal_3.displayAnimals()

    animal_1.displayCount()
