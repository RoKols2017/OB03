import pickle

# Базовый класс Animal
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        print(f"{self.name} ест.")


# Подклассы, наследующие от Animal
class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        print(f"{self.name} поет Кар-кар.")


class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print(f"{self.name} рычит Мяу-гав.")


class Reptile(Animal):
    def __init__(self, name, age, scales_type):
        super().__init__(name, age)
        self.scales = scales_type

    def make_sound(self):
        print(f"{self.name} шипит Ш-ш-ш.")


# Классы для сотрудников зоопарка
class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}.")
        animal.eat()


class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}.")


# Класс Zoo (композиция)
class Zoo():
    def __init__(self, name):
        self.animals = []
        self.employees = []

    def add_Bird(self, name, age, wing_span): # Создание птиц
        self.animals.append(Bird(name, age, wing_span))

    def add_Mammal(self, name, age, fur_color): # Создание млекопитающих
        self.animals.append(Mammal(name, age, fur_color))

    def add_Reptile(self, name, age, scales_type): # Создание рептилий
        self.animals.append(Reptile(name, age, scales_type))

    def add_ZooKeeper(self, name): # Создание кормильцев
        self.employees.append(ZooKeeper(name))

    def add_Veterinarian(self, name): # Создание ветеринаров
        self.employees.append(Veterinarian(name))

    # Полиморфизм
    def animal_sound(self): # Послушать звуки зоопарка
        for animal in self.animals:
            animal.make_sound()

    def feed_animals(self):  # Кормить животных
        for animal in self.animals:
            for employee in self.employees:
                if isinstance(employee, ZooKeeper):  # Проверка, что сотрудник - кормилец
                    employee.feed_animal(animal)

    def heal_animals(self):  # Лечить животных
        for animal in self.animals:
            for employee in self.employees:
                if isinstance(employee, Veterinarian):  # Проверка, что сотрудник - ветеринар
                    employee.heal_animal(animal)

    def save(self, filename): # Сохранить данные о зоопарке в файл
        with open(filename, 'wb') as f:
            pickle.dump(self, f)
            print(f"Зоопарк сохранен в файл {filename}")

    @staticmethod
    # это декоратор, который применяется к методу класса. Он указывает Python,
    # что этот метод является статическим и не должен иметь доступ к экземпляру класса
    # (то есть к объекту self) или к классу (через cls).
    def load(filename): # Загрузить данные о зоопарке из файла
        try:
            with open(filename, 'rb') as f:
                zoo = pickle.load(f)
                print(f"Зоопарк загружен из файла {filename}")
                return zoo
        except FileNotFoundError:
            print(f"{filename} такой файл отсутствует. Создаем новый зоопарк.")
            return Zoo()


# Создаем зоопарк
zoo = Zoo("Зоопарк Большого Города")

# Добавляем животных в зоопарк
zoo.add_Bird("Попугай", 2, 0.25)
zoo.add_Mammal("Тигр", 5, "Оранжевый с черными полосами")
zoo.add_Reptile("Крокодил", 7, "Твердая чешуя")

# Добавляем сотрудников в зоопарк
zoo.add_ZooKeeper("Иван")
zoo.add_Veterinarian("Мария")

# Демонстрация полиморфизма: послушаем, как издают звуки животные
print("\nЗвуки животных в зоопарке:")
zoo.animal_sound()

# Кормление животных
print("\nКормление животных:")
zoo.feed_animals()

# Лечение животных
print("\nЛечение животных:")
zoo.heal_animals()

# Сохранение состояния зоопарка в файл
zoo.save("zoo_data.pkl")

# Загрузка состояния зоопарка из файла
print("\nЗагружаем данные о зоопарке из файла...")
loaded_zoo = Zoo.load("zoo_data.pkl")

# Проверим, что данные были загружены
print("\nЗагруженные животные:")
for animal in loaded_zoo.animals:
    print(f"{animal.name} ({animal.__class__.__name__})")

