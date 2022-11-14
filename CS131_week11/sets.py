# Dorje Pradhan and Kameron Swingle 
# Python 1, CS 131
# November 7, 2022
# Sets in class activity

cast = {"lance", "gummy", "sinny"}

mySet =  set(["Mary", "Larry", "Carrie"]) 

for c in (cast): 
    print(c)

print("*" * 20)

# with the sorted
for c in sorted(cast):
    print(c)

print("*" * 20)

cast.add("Lance")

cast.discard("sinny")
cast.discard("happy") 

print(cast)

newSet = cast.union(mySet)

print(newSet)

cast.clear()

print(cast)

