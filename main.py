# # Створюємо головний (батьківський) клас - Транспорт
# class Transport:
#     """Class of vehicles, which includes all types of transport (land, air, sea, etc.)"""

#     # Create a constructor with parameters (speed, fuel, year of manufacture, distance)
#     def __init__(self, speed, fuel, year, distance):
#         self.speed = speed
#         self.fuel = fuel
#         self.year = year
#         self.distance = distance

#     # Create a method to describe the transport
#     def __str__(self):
#         return f'~~~Опис транспорту~~~\nШвидкість -> {self.speed} км/год\nТип палива ->  {self.fuel}\n' \
#                f'Рік випуску -> {self.year} р.\nВідстань -> {self.distance} км\n{"-" * 40}'

#     # Create a method to find the time (when the transport will arrive)
#     def finding_time(self):
#         time = self.distance / self.speed
#         hour = self.distance // self.speed
#         minute = time - hour
#         print("Знайдемо час, за який наш транспорт прибуде на місце призначення:")
#         if (minute >= 0.60) and (time >= 1 or time < 1):
#             minute -= 0.60
#             hour += 1
#             return f'При: S = {self.speed} км/год, V = {self.distance} км, ' \
#                    f't = {int(hour)} год {int(minute * 100)} хв\n{"-" * 40}'
#         else:
#             return f'При: S = {self.speed} км/год, V = {self.distance} км, ' \
#                    f't = {int(hour)} год {int(minute * 100)} хв\n{"-" * 40}'


# # Create a Car class, inherit from the Transport class
# class Car(Transport):
#     """Car class"""

#     # Create a constructor
#     def __init__(self, speed, fuel, year, distance, model, air_temperature):
#         Transport.__init__(self, speed, fuel, year, distance)
#         self.air_temperature = air_temperature
#         self.model = model

#     # Override the transport description method
#     def __str__(self):
#         return f'~~~Опис машини~~~\nШвидкість -> {self.speed} км/год\nТип палива ->  {self.fuel}\n' \
#                f'Модель -> {self.model}\nРік випуску -> {self.year} р.\nВідстань -> {self.distance} км\n' \
#                f'Температура на вулиці -> {self.air_temperature} C\n{"-" * 40}'

#     # Let's create a method to determine if the tires for the car need to be changed
#     def change_tires(self):
#         print(f'Чи потрібно змінювати резину, при t = {self.air_temperature}?')
#         if self.air_temperature <= 7:
#             return f'Вам треба змінити шини на зимові!\n{"-" * 40}'
#         else:
#             return f'Вам не треба змінити шини на зимові!\n{"-" * 40}'


# # Create the class Train, inherit from the class Transport
# class Train(Transport):
#     """Train class"""

#     # Create a constructor
#     def __init__(self, speed, fuel, year, distance, type_wagons, number_wagons):
#         Transport.__init__(self, speed, fuel, year, distance)
#         self.type_wagons = type_wagons
#         self.number_wagons = number_wagons

#     # Overriding the transport description method
#     def __str__(self):
#         return f'~~~Опис потягу~~~\nШвидкість -> {self.speed} км/год\nТип палива ->  {self.fuel}\n' \
#                f'Рік випуску -> {self.year} р.\nВідстань -> {self.distance} км\nВид вагону -> {self.type_wagons}' \
#                f'\nКількість вагонів -> {self.number_wagons}\n{"-" * 40}'

#     # Create a method to determine the maximum number of passengers
#     def max_number_passengers(self):
#         print("Знайдемо загальну кількість місць у потязі/експресі:")
#         if self.type_wagons == "Плацкарт".lower():
#             return f'Загальна к-сть місць у плацкарті = {54 * self.number_wagons}\n{"-" * 40}'
#         elif self.type_wagons == "Купе".lower():
#             return f'Загальна к-сть місць у купе = {36 * self.number_wagons}\n{"-" * 40}'
#         elif self.type_wagons == "Люкс".lower():
#             return f'Загальна к-сть місць у Люксі = {17 * self.number_wagons}\n{"-" * 40}'
#         elif self.type_wagons == "Сидячий".lower():
#             return f'Загальна к-сть місць у сидячому вагоні = {81 * self.number_wagons}\n{"-" * 40}'
#         else:
#             return f'Неправильний тип вагону!\n{"-" * 40}'


# # Create the Express class, inherit from the Train class
# class Express(Train):
#     """Class express"""

#     # Create a constructor
#     def __init__(self, speed, fuel, year, distance, type_wagons, number_wagons):
#         Train.__init__(self, speed, fuel, year, distance, type_wagons, number_wagons)

#     # Overriding the transport description method
#     def __str__(self):
#         return f'~~~Опис експресу~~~\nШвидкість -> {self.speed} км/год\nТип палива ->  {self.fuel}\n' \
#                f'Рік випуску -> {self.year} р.\nВідстань -> {self.distance} км\nВид вагону -> {self.type_wagons}' \
#                f'\nКількість вагонів -> {self.number_wagons}\n{"-" * 40}'


transport1 = Transport(60, "no", 2020, 25)
car1 = Car(90, "газ", 2000, 150, "Ford", 10)
car2 = Car(100, "бензин", 2020, 70, "Volkswagen", -5)
train1 = Train(110, "дизель", 1990, 300, "купе", 10)
train2 = Train(120, "дизель", 2004, 550, "плацкарт", 15)
express1 = Express(150, "дизель", 2020, 600, "люкс", 15)
express2 = Express(200, "дизель", 2019, 665, "сидячий", 8)

all_transport = [transport1, car1, car2, train1, train2, express1, express2]
for element in all_transport:
    print(element)
    print(element.finding_time())

train_express = [train1, train2, express1, express2]
for element in train_express:
    print(element.max_number_passengers())

cars = [car1, car2]
for element in cars:
    print(element.change_tires())
    