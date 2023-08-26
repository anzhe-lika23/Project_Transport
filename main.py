from Transport import Transport
from Car import Car
from Train import Train
from Express import Express


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
    