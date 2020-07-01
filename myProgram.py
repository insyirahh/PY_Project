print('Testing')
# Create a simple empty Vehicle class to represent cars,lorries or bus using the class keyword
class Vehicle:
   pass

# Create a variable for the Vehicle class object
class Vehicle:
    engine_capacity = "1,6 Turbo"

# Create a special(constructor) method for the class
class Vehicle:
    def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tank = type_of_tank
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity

# Object creation and printing the value of variables created
vios = Vehicle ('4','petrol', 5, 180)
print(vios.number_of_wheels)
print(vios.type_of_tank)
print(vios.seating_capacity)
print(vios.maximum_velocity)

# Create a function name drive and invoke the drive() function
def drive(self):
    print("The vehicle is in driving mode now.")


# Create a sub-class(child) of the Vehicle
class ElectricCar(Vehicle):
    def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
        Vehicle.__init__(self, number_of_wheels, 'electric', seating_capacity, maximum_velocity)

# Create an object from ElectricCar and invoke its drive() function
