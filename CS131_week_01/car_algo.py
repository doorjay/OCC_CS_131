# Car 1 is 30,000
# Car 2 is 40,000
# Car 1 mpg = 45mpg
# Car 2 mpg = 38mpg

# total cost of Car 1 in 10 years = 30,000(upfront cost) + 10(years) * 4(cost per gallon) * 15,000(miles driven) / 45(mpg)
# total cost of Car 2 in 10 years = 40,000(upfront cost) + 10(years) * 4(cost per gallon) * 15,000(miles driven) / 38(mpg)

car1 = 30000 + 10 * 4 * 15000 / 45
car2 = 40000 + 10 * 4 * 15000 / 38

print("Car 1 total cost: %0.2f" % (car1))
print("Car 2 total cost: %0.2f" % (car2))

if car1 < car2 :
  print("\nI choose the first car!")
else :
  print("\nI choose the second car!")