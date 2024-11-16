# Lee Fawkes
# Andrew Emily
# SDEV-220 Module 3 Lab - Case Study: Lists, Functions, and Classes

# My approach here might not precisely align with the assignment, but creating 
# an instance of a Vehicle object only makes sense to me if we're tracking and
# manipulating discrete vehicles. This program will take a string as a name of
# a vehicle, but a real-world application could key on a VIN or license plate
# instead.

class Vehicle(object):
    def __init__(self, vehicle_type):
        """Assumes type a string. Create a vehicle."""
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, name, year, make, model, doors, roof_type):
        super().__init__("car")
        self.name = name
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof_type = roof_type

    def __str__(self):
        return f"""
        Name: {self.name}
        Year: {self.year}
        Make: {self.make}
        Model: {self.model}
        Number of doors: {self.doors}
        Roof type: {self.roof_type}
        """
        

cars = []
choice = 0

print("This program will take in input about cars, store that information, and allow information about cars to be displayed.")

while choice != 4:
    try:
        print("1. Enter car")
        print("2. Display cars")
        print("3. Display info about car")
        print("4. Exit")
        choice = int(input("Enter choice (1-4): "))
        if choice == 1:
            name = input("Enter car name (IE \"Mom's car\" or \"Christine\"): ")
            while True:
                try:
                    year = int(input("Enter model year: "))
                    break
                except ValueError:
                    print("Please enter an integer year value, preferably an integer that corresponds with a year in which cars were made.")
                    print("Or you can enter some wacky integer value for an imaginary model year. You do you.")

            make = input("Enter the vehicle make (IE \"Toyota\"): ")
            model = input("Enter the vehicle model (IE \"Supra\"): ")

            while True:
                try:
                    doors = int(input("Enter the number of doors (2-5): "))
                    # I know the assignment says 2 or 4, but the Mazda RX-8 has 3 doors, and a station wagon would have 5
                    if 2 <= doors <= 5:
                        break
                    print("Please enter an integer from 2-5")
                except ValueError:
                    print("Please enter an integer from 2-5")

            while True:
                # Again sorry my program differs slightly from the assignment specification,
                # But I used to have a 1987 Toyota Supra Turbo Targa, so gotta be able to enter that.
                roof_type = input("Enter the roof type (hard top, sunroof, convertible, targa): ")
                if roof_type in ["hard top", "sunroof", "convertible", "targa"]:
                    break
                print("Please enter a roof type exactly as specified in the input prompt.")

            new_car = Automobile(name, year, make, model, doors, roof_type)
            cars.append(new_car)
            print("Car added.")

        elif choice == 2:
            for car in cars:
                print(car.name)

        elif choice == 3:
            car_search = input("Enter car name: ")
            found = 0

            for car in cars:
                if car.name == car_search:
                    print(car)
                    found = 1
            else:
                if found == 0:
                    print("Car not found.")
        
        elif choice not in [1, 2, 3, 4]:
            print("Please enter a number from 1-4.")

    except ValueError:
        print("Please enter a number from 1-4.")

        
