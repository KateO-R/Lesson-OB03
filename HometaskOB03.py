class Animal():
    def __init__(self, specie, sound):
        self.specie = specie
        self.sound = sound

    def make_sound(self):
        pass


class Bird(Animal):
    def __init__(self, specie, sound):
        super().__init__(specie, sound)

    def make_sound(self):
        print(f"{self.specie} - {self.sound}")


class Mammal(Animal):
    def __init__(self, specie, sound):
        super().__init__(specie, sound)

    def make_sound(self):
        print(f"{self.specie} - {self.sound}")


class Reptile(Animal):
    def __init__(self, specie, sound):
        super().__init__(specie, sound)

    def make_sound(self):
        print(f"{self.specie} - {self.sound}")


class Staff:
    def __init__(self, name):
        self.name = name


class ZooKeeper(Staff):
    def __init__(self, name):
        super().__init__(name)

    def feed_animal(self, animal):
        print(f"{animal.specie} has been fed by {self.name}")


class Veterinarian(Staff):
    def __init__(self, name):
        super().__init__(name)

    def heal_animal(self, animal):
        print(f"{animal.specie} is  healthy now thanks to {self.name}")


class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Animal {animal.specie} has been successfully added to the Zoo {self.name}")


    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"Employee {staff_member.name} has been employed to the Zoo {self.name}")

    def show_animals(self):
        print(f"Animals in {self.name}:")
        for animal in self.animals:
            animal.make_sound()

    def show_staff(self):
        print(f"Staff in {self.name}:")
        for staff_member in self.staff:
            print(f"{staff_member.name}")


zoo = Zoo("SuperZoo")

bird = Bird("Cock", "cuckoo")
monkey = Mammal("Monkey", "croak")
cobra = Reptile("Cobra", "hiss")
zoo.add_animal(bird)
zoo.add_animal(monkey)
zoo.add_animal(cobra)

zookeeper = ZooKeeper("Jack")
veterinarian = Veterinarian("Jill")
zoo.add_staff(zookeeper)
zoo.add_staff(veterinarian)

zoo.show_animals()
zoo.show_staff()

zookeeper.feed_animal(bird)
veterinarian.heal_animal(monkey)

