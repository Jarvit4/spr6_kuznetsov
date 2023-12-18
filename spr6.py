from abc import ABC, abstractmethod

# Базовий клас "Літак"
class Airplane(ABC):
    def get_description(self):
        pass

    def get_cost(self):
        pass

# Конкретний літак
class BasicAirplane(Airplane):
    def get_description(self):
        return "Основний літак"

    def get_cost(self):
        return 1000000.0

# Декоратор - клас, який додає функціональність
class AirplaneDecorator(Airplane):
    def __init__(self, airplane):
        self.airplane = airplane

    def get_description(self):
        return self.airplane.get_description()

    def get_cost(self):
        return self.airplane.get_cost()

# Декоратор для додавання двигуна відмінної потужності
class PowerfulEngineDec(AirplaneDecorator):
    def get_description(self):
        return super().get_description() + ", з потужним двигуном"

    def get_cost(self):
        return super().get_cost() + 50000.0

# Декоратор для додавання покращеної авіоніки
class AdvancedAvionicsDec(AirplaneDecorator):
    def get_description(self):
        return super().get_description() + ", з покращеною авіонікою"

    def get_cost(self):
        return super().get_cost() + 75000.0


#Основний літак
basic_airplane = BasicAirplane()
print("Опис:", basic_airplane.get_description())
print("Вартість: $", basic_airplane.get_cost())

#Потужний двигун
powerful_engine_airplane = PowerfulEngineDec(basic_airplane)
print("Опис:", powerful_engine_airplane.get_description())
print("Вартість: $", powerful_engine_airplane.get_cost())

#Авіоніка
advanced_avionics_airplane = AdvancedAvionicsDec(basic_airplane)
print("Опис:", advanced_avionics_airplane.get_description())
print("Вартість: $", advanced_avionics_airplane.get_cost())

#Потужний двигуна та покращена авіоніка
powerful_and_advanced_airplane = AdvancedAvionicsDec(PowerfulEngineDec(basic_airplane))
print("Опис:", powerful_and_advanced_airplane.get_description())
print("Вартість: $", powerful_and_advanced_airplane.get_cost())
