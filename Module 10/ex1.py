class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.current_floor = bottom_floor
    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f'You are now on floor {self.current_floor}')
        else:
            print("You are already at the top floor.")
    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor = self.current_floor - 1
            print(f'You are now on floor {self.current_floor}')
        else:
            print("You are already at the bottom floor.")
    def go_to_floor(self, dest):
        if dest < self.current_floor:
            while dest < self.current_floor:
                self.floor_down()
        elif dest > self.current_floor:
            while dest > self.current_floor:
                self.floor_up()