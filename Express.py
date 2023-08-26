from Train import Train


# Create the Express class, inherit from the Train class
class Express(Train):
    """Class express"""

    # Create a constructor
    def __init__(self, speed, fuel, year, distance, type_wagons, number_wagons):
        Train.__init__(self, speed, fuel, year, distance, type_wagons, number_wagons)

    # Overriding the transport description method
    def __str__(self):
        return f'~~~Опис експресу~~~\nШвидкість -> {self.speed} км/год\nТип палива ->  {self.fuel}\n' \
               f'Рік випуску -> {self.year} р.\nВідстань -> {self.distance} км\nВид вагону -> {self.type_wagons}' \
               f'\nКількість вагонів -> {self.number_wagons}\n{"-" * 40}'
