"""Пример взаимодействия объектов классов - ассоциация."""


class Person:
    """Класс, представляющий человека."""

    def __init__(self, name: str):
        self.name = name

    def drive(self, car):
        """Человек может управлять автомобилем."""
        print(f"{self.name} is driving the {car.make} {car.model}.")


class Car:
    """Класс, представляющий автомобиль."""

    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model


if __name__ == "__main__":
    # Создаем объекты классов
    john = Person("John")
    tesla = Car("Tesla", "Model 3")

    # Объект Person (John) взаимодействует с объектом Car (Tesla) через метод
    john.drive(tesla)
