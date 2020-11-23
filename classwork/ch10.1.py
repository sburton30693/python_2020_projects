# Spencer Burton
# Classes and OOP Introduction

class Car() :

    # Special Method for declaring stuff
    def __init__(self) :
        self.color = ""
        self.size  = ""
        self.brand = ""
        self.make  = ""
        self.year  = ""
        self.type  = ""
        self.price = 0.0
        self.tire_brand  = ""
        self.tire_size   = ""
        self.drive_train = ""
        self.fuel_type   = ""
        #self.radio  = Radio()
        #self.engine = Engine()

        self.color = input("What color is the car? ")
        #self.size  = input("How big is the car? ")
        #self.brand = input("What brand is the car? ")
        #self.make  = input("What make is the car? ")
        #self.year  = input("What year is the car? ")
        #self.type  = input("What type is the car? ")
        #self.price = input("What price is the car? ")
        #self.tire_brand  = input("What brand are the tires? ")
        #self.tire_size   = input("What size are the tires? ")
        #self.drive_train = input("What is the drive train of the car? ")
        #self.fuel_type   = input("What type of fuel does the car use? ")

    def display(self) :
        if self.color != "" :
            print(self.color)


class Engine() :

    def __init__(self) :
        self.cylinder = ""
        self.cylinder_ornt = ""
        self.mpg = ""

        self.cylinder = input("How many cylinders will the engine have? ")
        self.cylinder_ornt = input("What orientation are the cylinders? ")
        self.mpg = input("How many miles per gallon? ")



def main() :
    my_dream_car = Car()
    my_dream_car.display()

main()
