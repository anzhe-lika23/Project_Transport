# Створюємо головний (батьківський) клас - Транспорт
class Transport:
    """Class of vehicles, which includes all types of transport (land, air, sea, etc.)"""

    # Create a constructor with parameters (speed, fuel, year of manufacture, distance)
    def __init__(self, speed, fuel, year, distance):
        self.speed = speed
        self.fuel = fuel
        self.year = year
        self.distance = distance

    # Create a method to describe the transport
    def __str__(self):
        return f'~~~Опис транспорту~~~\nШвидкість -> {self.speed} км/год\nТип палива ->  {self.fuel}\n' \
               f'Рік випуску -> {self.year} р.\nВідстань -> {self.distance} км\n{"-" * 40}'

    # Create a method to find the time (when the transport will arrive)
    def finding_time(self):
        time = self.distance / self.speed
        hour = self.distance // self.speed
        minute = time - hour
        print("Знайдемо час, за який наш транспорт прибуде на місце призначення:")
        if (minute >= 0.60) and (time >= 1 or time < 1):
            minute -= 0.60
            hour += 1
            return f'При: S = {self.speed} км/год, V = {self.distance} км, ' \
                   f't = {int(hour)} год {int(minute * 100)} хв\n{"-" * 40}'
        else:
            return f'При: S = {self.speed} км/год, V = {self.distance} км, ' \
                   f't = {int(hour)} год {int(minute * 100)} хв\n{"-" * 40}'
