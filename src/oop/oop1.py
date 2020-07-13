# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# This is the BASE CLASS
class Vehicle:
    pass

# The following two classes inherit from the Vehicle class
class FlightVehicle(Vehicle):
    pass

class GroundVehicle(Vehicle):
    pass

# The following two classes inherit from the GroundVehicle class
class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass

# The following two classes inherit from the FlightVehicle class
class Starship(FlightVehicle):
    pass

class Airplane(FlightVehicle):
    pass
