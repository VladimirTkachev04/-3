class Transport:
    def __init__(self, speed: int, name: str, passengers: int, fuel: int):
        self.speed = speed
        self.name = name
        self.passengers = passengers
        self.fuel = fuel
class Bysicle(Transport):
    def __init__(self, speed: int, name: str, passengers: int, fuel: int):
        super().__init__(speed, name, passengers, fuel)
    def move(self):
        print(f'Велосипед {self.name} движеться со скоросью {self.speed} с возможностью везти {self.passengers} пассажиров\nДля этого транспорта требуется {self.fuel}л. топлива.')
class Car(Transport):
    def __init__(self, speed: int, name: str, passengers: int, fuel: int):
        super().__init__(speed, name, passengers, fuel)
    def full_fuel(self):
        self.fuel += 10
        print('Автомобиль заправлен на 10 литров')
    def move(self):
        print(f'{self.name} может проехать {self.fuel*10} км и везти {self.passengers} пассажиров.\nСо скоростью {self.speed}')
class Truck(Transport):
    def __init__(self, speed: int, name: str, passengers: int, fuel: int):
        super().__init__(speed,name,passengers,fuel)
    def full_fuel(self):
        self.fuel += 10
        print('Грузовик заправлен на 10 литров')
    def move(self):
         print(f'{self.name} может проехать {self.fuel*5} км и везти {self.passengers} пассажиров.\nСо скоростью {self.speed}')
bysicle = Bysicle(15, 'Stels', 1, 0)
car = Car(60,'BMV',3, 5)
truck = Truck(45,'Volvo', 4, 20)
Reqest = int(input('Выберите транспорт:\nВелосипед - 1\nАвтомобиль - 2\nГрузовик - 3\n'))
if Reqest == 1:
    bysicle.move()
elif Reqest == 2:
    print("Топливо машины:", car.fuel)
    car.full_fuel()
    car.move()
elif Reqest == 3:
    print("Топливо грузовика", truck.fuel)
    truck.full_fuel()
    truck.move()
else:
    print('Выбран не верный номер транспорта.')