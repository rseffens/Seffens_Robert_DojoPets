class Ninja:
    def __init__(self, first_name, last_name, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet

    def info(self):
        print(f'first name: {self.first_name}')
        print(f'last name: {self.last_name}')
        self.pet.info()

    def walk(self):
        self.pet.play()
        return self

    def feed (self):
        self.pet.eat()
        return self

    def bathe (self):
        self.pet.noise()
        return self

class Pet:
    def __init__(self, name, type, health = 100, energy = 50):
        self.name = name
        self.type = type
        self.health = health
        self.energy = energy

    def info(self):
        print(f'name: {self.name}')
        print(f'type: {self.type}')
        print(f'health: {self.health}')
        print(f'energy: {self.energy}')

    def sleep(self):
        self.health += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        return self

    def noise(self):
        print("woof")
        return self