class Car:
    def __init__(self, license_plate, maximum_speed):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0
    def accelerate(self, accel):
        if accel >= 0:
            self.current_speed = accel
        else:
            self.current_speed = 0
        if accel >= self.maximum_speed:
            self.current_speed = self.maximum_speed
    def drive(self, time):
        if time > 0:
            self.travelled_distance += time * self.current_speed
class ElectricCar(Car):
    def __init__(self, license_plate, maximum_speed, battery_capacity):
        super().__init__(license_plate, maximum_speed)
        self.battery_capacity = battery_capacity
class GasolineCar(Car):
    def __init__(self, license_plate, maximum_speed, tank_volume):
        super().__init__(license_plate, maximum_speed)
        self.tank_volume = tank_volume