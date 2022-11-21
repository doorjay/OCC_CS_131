# Dorje Pradhan
# Python 1, CS 131
# November 21, 2022
# Implement a class Student and save it
# Student has a name and total quiz score
# supply an appropriate constructor
# create getters and setters
# create addQuiz() and getAverageScore()

class Student :

    # Student constructor
    def __init__(self, name = "", quiz = 0, numOfQuiz = 0):
        self._name = name 
        self._quiz = quiz
        self._numOfQuiz = numOfQuiz

    # accessors ----------------------------------------
    def getName(self):
        return self._name 

    def getTotalScore(self): 
        return self._quiz

    def getAverageScore(self):
        return self._quiz / self._numOfQuiz

    # mutators -----------------------------------------
    def addQuiz(self, score) :
        self._quiz += score
        self._numOfQuiz += 1