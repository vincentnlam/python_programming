class Vehicle:
    def __init__(self, name, wheels):
        self.name = name
        self.wheels = wheels

    def has_wheels(self):
        return self.wheels
    
    def move_forward(self):  
        print(f"{self.name} moving_forward")
    
    def move_backward(self):
        print(f"{self.name} moving_backward")

    def turn_left(self):
        print(f"{self.name} turn_left")

    def turn_right(self):
        print(f"{self.name} turn_right")

class Car(Vehicle):
    def __init__(self, name, wheels):
        self.name = name
        self.wheels = wheels

class Truck(Vehicle):
    def __init__(self, name, wheels):
        self.name = name
        self.wheels = wheels

if __name__ == "__main__":
    my_car = Car("car1", 4)
    my_truck = Truck("truck1", 8)
    print(my_car.has_wheels())
    print(my_truck.has_wheels())
    my_car.move_forward()
    my_car.turn_left()
    my_truck.move_forward()
    my_truck.turn_left()