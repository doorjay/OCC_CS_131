# Dorje Pradhan
# September 21, 2022
# Python 1, CS 131
# Mess with the string Hello World

str = "  Hello, World  "

print("The number of l's is", str.count('l'))
print("***" + str.strip() + "***")
print("***" + str.lstrip() + "***")
print("***" + str.rstrip() + "***")
print(str.strip().replace("o", "***"))