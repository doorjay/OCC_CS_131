# Dorje Pradhan
# Python 1, CS 131
# November 21, 2022
# Test the Student class here!

from IC_Lab2 import Student

# Define a student object
s1 = Student("Jon") 

# Add the first score
s1.addQuiz(90) 
# Add the second score
s1.addQuiz(100) 

print("The total score for", s1.getName(), "is", s1.getTotalScore(),
      "and the average is", s1.getAverageScore())