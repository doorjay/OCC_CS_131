myDictionary = {}
print("the length of the dictionary is", len(myDictionary)) 
anotherDictionary = {"May" : 2145523, "Cory" : 3559912, "Sara" : 4329898}
#adding elements
myDictionary["Alan"]= 4533344
myDictionary["Khoi"]=343233

#adding elements
anotherDictionary["Ellen"] = 4349098

print("the length of the dictionary is", len(myDictionary))
print("the length of the dictionary is ", len(anotherDictionary))

print("May's number is ", anotherDictionary["May"])



for key in anotherDictionary: 
    print("key:",end="") 
    print(key)
    print("value:",end="" ) 
    print(anotherDictionary[key]) 

anotherDictionary.pop("Sara") 
ellenNumber = anotherDictionary.pop("Ellen")

print("the popped number was: ", ellenNumber)



print("*"*40) 
print("My Contacts:") 
for key in sorted(anotherDictionary) :
    print("%-10s %d" % (key, anotherDictionary[key]))


print("Another way to interate and print")

for item in anotherDictionary.items() :
    print(item[0], item[1]) 