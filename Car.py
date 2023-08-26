from Transport import Transport


# Create a Car class, inherit from the Transport class
class Car(Transport):
    """Car class"""

    # Create a constructor
    def __init__(self, speed, fuel, year, distance, model, air_temperature):
        Transport.__init__(self, speed, fuel, year, distance)
        self.air_temperature = air_temperature
        self.model = model

    # Override the transport description method
    def __str__(self):
        return f'~~~Опис машини~~~\nШвидкість -> {self.speed} км/год\nТип палива ->  {self.fuel}\n' \
               f'Модель -> {self.model}\nРік випуску -> {self.year} р.\nВідстань -> {self.distance} км\n' \
               f'Температура на вулиці -> {self.air_temperature} C\n{"-" * 40}'

    # Let's create a method to determine if the tires for the car need to be changed
    def change_tires(self):
        print(f'Чи потрібно змінювати резину, при t = {self.air_temperature}?')
        if self.air_temperature <= 7:
            return f'Вам треба змінити шини на зимові!\n{"-" * 40}'
        else:
            return f'Вам не треба змінити шини на зимові!\n{"-" * 40}'
