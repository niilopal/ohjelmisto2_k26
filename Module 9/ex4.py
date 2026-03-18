import random
class Car:
    def __init__(self, license_plate, maximum_speed, current_speed=0, travelled_distance=0):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance
    def accelerate(self, accel):
        if accel + self.current_speed >= 0:
            self.current_speed += accel
        else:
            self.current_speed = 0
        if accel + self.current_speed >= self.maximum_speed:
            self.current_speed = self.maximum_speed
    def drive(self, time):
        if time > 0:
            self.travelled_distance += time * self.current_speed
def race(cars):
    x = 0
    while x == 0:
        for i in cars:
            i.accelerate(random.randint(-10, 15))
            i.drive(1)
            if i.travelled_distance > 10000:
                x = 1
                break
    for i in cars:
        print(f'Car: {i.license_plate}\n  Travelled: {i.travelled_distance}km')

cars = [Car("AAA-000", 120), Car("AAA-000", 120), Car("AAA-000", 120)]
race(cars)
