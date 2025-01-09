class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        print(f"{self.name} ест.")

class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        print("Кар-кар.")

class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print("Мяу-гав.")

class Reptile(Animal):
    def __init__(self, name, age, scales):
        super().__init__(name, age)
        self.scales = scales

    def make_sound(self):
        print("Ш-ш-ш.")


class Zoo():
    def __init__(self, name):
        self.name = name
        self.animals = []


animals = [Bird("Курица", 1, 0.5),
           Mammal("Котопес", 3, "Серый"),
           Reptile("Ящерица", 0, "Кожа")]


for animal in animals:
    animal.make_sound()