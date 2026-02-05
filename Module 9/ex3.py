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
car = Car("ABC-123", 142)
print(f"Initial distance: {car.travelled_distance} km")
car.current_speed = 60
car.drive(1.5)
print(f"Distance after driving 1.5 hours at 60 km/h: {car.travelled_distance} km")