class Car:
    def __init__(self, color, wheels = 4):
        self.color = color
        self.number_of_wheels = wheels

    def __str__(self):
        return(f"The car is {self.color}, it has {self.number_of_wheels} wheels")

    def honk(self):
        print("HONK!!!")
