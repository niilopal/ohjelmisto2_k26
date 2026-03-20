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
class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars
    def hour_passes(self):
        for i in self.cars:
            i.accelerate(random.randint(-10, 15))
            i.drive(1)
    def print_status(self):
        print(f'|{"License":10s}|{"Speed":10s}|{"Distance":10s}|')
        print("----------------------------------")
        for i in self.cars:
            print(f'|{i.license_plate:10s}|{i.current_speed:10d}|{i.travelled_distance:10d}|')
    def race_finished(self):
        for i in self.cars:
            if i.travelled_distance >= self.distance:
                return True
        return False