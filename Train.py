from Transport import Transport


# Create the class Train, inherit from the class Transport
class Train(Transport):
    """Train class"""

    # Create a constructor
    def __init__(self, speed, fuel, year, distance, type_wagons, number_wagons):
        Transport.__init__(self, speed, fuel, year, distance)
        self.type_wagons = type_wagons
        self.number_wagons = number_wagons

    # Overriding the transport description method
    def __str__(self):
        return f'~~~Опис потягу~~~\nШвидкість -> {self.speed} км/год\nТип палива ->  {self.fuel}\n' \
               f'Рік випуску -> {self.year} р.\nВідстань -> {self.distance} км\nВид вагону -> {self.type_wagons}' \
               f'\nКількість вагонів -> {self.number_wagons}\n{"-" * 40}'

    # Create a method to determine the maximum number of passengers
    def max_number_passengers(self):
        print("Знайдемо загальну кількість місць у потязі/експресі:")
        if self.type_wagons == "Плацкарт".lower():
            return f'Загальна к-сть місць у плацкарті = {54 * self.number_wagons}\n{"-" * 40}'
        elif self.type_wagons == "Купе".lower():
            return f'Загальна к-сть місць у купе = {36 * self.number_wagons}\n{"-" * 40}'
        elif self.type_wagons == "Люкс".lower():
            return f'Загальна к-сть місць у Люксі = {17 * self.number_wagons}\n{"-" * 40}'
        elif self.type_wagons == "Сидячий".lower():
            return f'Загальна к-сть місць у сидячому вагоні = {81 * self.number_wagons}\n{"-" * 40}'
        else:
            return f'Неправильний тип вагону!\n{"-" * 40}'
