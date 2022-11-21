##
#  This module defines the car class.
#

##
#  A car that tracks its fuel consumption as it is driven.
class Car:
    ## Constructs a new car with a given fuel efficiency.
    #  @param fuel_efficiency the fuel efficiency of the car
    #
    def __init__(self, mpg = 1):
      self._mpg = mpg
      self._fuelLevel = 0

    ## Add gas to the car's tank.
    #  @param amount the amount of gas to add
    def addGas(self, gas):
      self._fuelLevel += gas

    ## Add gs to the car's tank.
    # @param amount the amount of gas to add
    def addGas(self, gas):
      self._fuelLevel += gas

    ## Simulate driving the car.
    #  @param distance the distance the car is driven
    def drive(self, distance):
      self._fuelLevel -= distance / self._mpg

    ## Get the amount of gas in the tank.
   #  @return the amount of gas in the tank
    def getGasLevel(self):
      return self._fuelLevel

