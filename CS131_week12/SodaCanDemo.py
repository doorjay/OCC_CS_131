# Dorje Pradhan 
# November 24, 2022
# Python 1, CS 131
# Learning Classes in python!

# Create a tester file, create two objects: 
#    One with a height of 8 and radius of 4
#    One with a height of 5 and radiys of 2

from SodaCan import *

def main() :
    # Instantiate two SodaCan objects
    fanta = SodaCan(8, 4)
    sprite = SodaCan(5, 2)

    # initialize variables for Surface area and volume
    fantaSA = fanta.getSurfaceArea()
    fantaVolume = fanta.getVolume()

    spriteSA = sprite.getSurfaceArea()
    spriteVolume = sprite.getVolume()

    # output the volume and surface area of the two sodas!

    # Fanta
    print("The surface area of the fanta can (h = %d, r = %d) is: %0.2f"\
          % (fanta.getHeight(), fanta.getRadius(), fantaSA))
    print("The volume of the can of fanta (h = %d, r = %d) is: %0.2f"\
          % (fanta.getHeight(), fanta.getRadius(), fantaVolume))

    # Sprite
    print("The surface area of the sprite can (h = %d, r = %d) is: %0.2f"\
          % (sprite.getHeight(), sprite.getRadius(), spriteSA))
    print("The volume of the can of sprite (h = %d, r = %d) is: %0.2f"\
          % (sprite.getHeight(), sprite.getRadius(), spriteVolume))


main()