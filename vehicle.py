class Vehicle:
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed
    
    def display_info(self):
        print(f"Color: {self.color}")
        print(f"Speed: {self.speed} km/h")


class Car(Vehicle):
    def __init__(self, color, speed, brand):
        super()._init_(color, speed)
        self.brand = brand
    
    def display_info(self):
        super().display_info()
        print(f"Brand: {self.brand}")


print("Vehicle Object:")
v1 = Vehicle("Red", 80)
v1.display_info()


print("Car Object:")
c1 = Car("Blue", 120, "Toyota")
c1.display_info()

 