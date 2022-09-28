# Dorje Pradhan
# Python 1, CS 131
# September 26, 2022
# Write a program that computes information related
# to a sequence of grades obtained from the user. It 
# computes the number of passing and failing grades, 
# computes the average grade and finds the highest and 
# lowest grade.

SENTINEL = -1
grade = 0
passing = 0
failing = 0
average = 0
count = 0
highest = 0
lowest = 1000 # a value larger than any should be entered

while grade != SENTINEL :
    grade = int(input("Please enter a grade or -1 to quit: "))

    # check for sentinel first
    if (grade != -1) : 
        count += 1  # incriment count
        average += grade

        # check for passsing or failing
        if grade >= 60 :
            passing += 1
        else :
            failing += 1

        # finding highest and lowest grades
        if (grade > highest) :
            highest = grade
        if (grade < lowest) :
            lowest = grade

        # make sure to give a value to lowest
        

average /= count

print("The average grade is: %.2f" %average)
print("The number of passing grades is:", passing)
print("The number of failing grades is:", failing)
print("The highest grade is: %.2f" %highest)
print("The lowest grade is: %.2f" %lowest)