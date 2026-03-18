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
    car0 = Car(cars[0], cars[1])
    car1 = Car(cars[2], cars[3])
    car2 = Car(cars[4], cars[5])
    mdist = 0
    while mdist < 10000:
        car0.accelerate(random.randint(-10, 15))
        car1.accelerate(random.randint(-10, 15))
        car2.accelerate(random.randint(-10, 15))
        car0.drive(1)
        car1.drive(1)
        car2.drive(1)
        if car0.travelled_distance > car1.travelled_distance and car0.travelled_distance > car2.travelled_distance:
            mdist = car0.travelled_distance
        elif car1.travelled_distance > car0.travelled_distance and car1.travelled_distance > car2.travelled_distance:
            mdist = car1.travelled_distance
        elif car2.travelled_distance > car0.travelled_distance and car2.travelled_distance > car1.travelled_distance:
            mdist = car2.travelled_distance
    print(f'Car: {car0.license_plate}\nTravelled: {car0.travelled_distance}km\nCar: {car1.license_plate}\nTravelled: {car1.travelled_distance}km\nCar: {car2.license_plate}\nTravelled: {car2.travelled_distance}km\n')
cars = ['AAA-000', 120, 'AAA-001', 120, 'AAA-002', 120]
race(cars)
