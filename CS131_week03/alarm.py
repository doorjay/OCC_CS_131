# Dorje Pradhan
# Spetember 12, 2022
# Python 1, CS 133
# Set someones alarm in millitary time

time = int(input("What is the current time (in military format)? "))
hours = int(input("After how many hours should the alarm go off? "))

alarm = (time + hours) % 24

print("The alarm should go off at", alarm)
