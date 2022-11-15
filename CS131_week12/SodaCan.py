# Dorje Pradhan 
# November 24, 2022
# Python 1, CS 131
# Learning Classes in python!

# Implemenet a class named SodaCan
# implement the methods getSurfaceArea() and getVolume
# In the constructor, supply the height and radius of the can

import math

class SodaCan :

    # Constructors ------------------------------

    def __init__(self, height = 1, radius = 1) :
        self.height = height
        self.radius = radius

    # Member functions --------------------------------

    # getters ------------------------------------

    def getHeight(self) :
        return self.height

    def getRadius(self) :
        return self.radius

    # Returns the surface area of the calling object
    def getSurfaceArea(self) :
        return (2 * math.pi * self.radius ** 2) + (2 * math.pi * self.radius * self.height)
        
    # Returns the volume of the calling object
    def getVolume(self) :
        return math.pi * self.radius ** 2 * self.height 


    # setters -------------------------------------

    def setHeight(self, height) :
        self.height = height 

    def setRadius(self, radius) :
        self.radius = radius