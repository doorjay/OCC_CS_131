# Dorje Pradhan
# Python 1 CS 133
# September 7, 2022
# Print the perimeter and diagonal in inches

import math

# "input"
paperW = 8.5
paperH = 11

# process
perim = paperW * 2 + paperH * 2
diagonal = math.sqrt(8.5**2 + 11**2) # uses pyth thereom to determine diagonal

# output
print("The perimeter is", perim, "inches.")
print("The length of the diagonal is", diagonal, "inches.")
