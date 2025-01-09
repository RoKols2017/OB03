import pickle


# 1. Базовый класс Animal
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        print(f"{self.name} is eating.")

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.age})"


# 2. Подклассы, наследующие от Animal
class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        return f"{self.name} chirps."


class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        return f"{self.name} roars."


class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type

    def make_sound(self):
        return f"{self.name} hisses."


# 3. Полиморфизм: функция animal_sound
def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())


# 4. Класс Zoo (композиция)
class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_employee(self, employee):
        self.employees.append(employee)

    def save(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)
            print(f"Zoo saved to {filename}")

    @staticmethod
    def load(filename):
        try:
            with open(filename, 'rb') as f:
                zoo = pickle.load(f)
                print(f"Zoo loaded from {filename}")
                return zoo
        except FileNotFoundError:
            print(f"{filename} not found. Returning a new zoo.")
            return Zoo()


# 5. Классы для сотрудников зоопарка
class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} is feeding {animal.name}.")
        animal.eat()


class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} is healing {animal.name}.")


# Пример использования:
if __name__ == "__main__":
    # Создаем зоопарк или загружаем существующий
    zoo = Zoo.load("zoo_data.pkl")

    # Создаем животных
    bird = Bird("Parrot", 2, "Large")
    mammal = Mammal("Lion", 5, "Golden")
    reptile = Reptile("Snake", 3, "Smooth")

    # Добавляем животных в зоопарк
    zoo.add_animal(bird)
    zoo.add_animal(mammal)
    zoo.add_animal(reptile)

    # Создаем сотрудников
    zookeeper = ZooKeeper("John")
    vet = Veterinarian("Alice")

    # Добавляем сотрудников в зоопарк
    zoo.add_employee(zookeeper)
    zoo.add_employee(vet)

    # Действия сотрудников
    zookeeper.feed_animal(bird)
    vet.heal_animal(reptile)

    # Полиморфизм: звучание животных
    animal_sound([bird, mammal, reptile])

    # Сохраняем состояние зоопарка
    zoo.save("zoo_data.pkl")
