# Dorje Pradhan
# September 19, 2022
# Python 1, CS 131
# Determine whether a rope will snap when whirling a mass.

rotation_speed = int(input("Enter the rotation speed: "))

BREAK_POINT = 60
mass = 2
radius = 3

# Formula for tension
tension = mass * (rotation_speed ** 2) / radius

if tension > BREAK_POINT :
   print("The rope breaks.")
else :
   print("The rope does not break.")

