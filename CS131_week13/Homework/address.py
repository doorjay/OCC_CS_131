##
#  This module defines the Address class.
#

##
#  An address that stores house number, street number, optional apartment
#  number, city, state and postal code.
class Address:
    ## Constructs an address without an apartment number.
   #  @param house the house number
   #  @param street the street name
   #  @param apt the apartment number
   #  @param city the name of the city
   #  @param state the name of the state
   #  @param postal the postal code
   #
   def __init__(self, house, street, city, state, postal, apt = 0):
      self._house = house
      self._street = street
      self._apt = apt
      self._city = city
      self._state = state
      self._postal = postal

   ## Prints an address.
   #
   def printAddress(self):
      if self._apt != 0:
         print(self._apt, end = "-")
         
      print(self._house, self._street)
      print(f"{self._city},", self._state, self._postal)
      print()
     
   ## Determine if one address comes before another by postal code.
   #  @param other the other address to consider for comparison
   #  @return True if self is less than other, False otherwise
   #
   def comesBefore(self, otherAddress):
      return self._postal < otherAddress._postal
