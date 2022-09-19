# Dorje Pradhan
# September 19, 2022
# Python 1, CS 131
# Given the following paragraph:
# "Debating me breeding be answered an he. Spoil event was words her off cause
# any. Tears woman which no is world miles woody. Wished be do mutual except
# in effect answer. Had friendship thoroughly cultivated son imprudence 
# connection. Windows because concern its. Law allow saved views hills day
# ten. Examine waiting his evening day passage proceed. "

# Write a program that finds the number of times the following substrings 
# apper in the text:
#	“un”
#	“an”
#	“in”
#	“he”

paragraph = """Debating me breeding be answered an he. Spoil event was words her
            off cause any. Tears woman which no is world miles woody. Wished be do
            mutual except in effect answer. Had friendship thoroughly cultivated son
            hills day ten. Examine waiting his evening day passage proceed."""
            
num_un = paragraph.count('un')
num_an = paragraph.count('an')
num_in = paragraph.count('in')
num_he = paragraph.count('he')

index_un = paragraph.find("un")
index_an = paragraph.find("an")
index_in = paragraph.find("in")
index_he = paragraph.find("he")

print("In the following paragraph:\n")
print("----------------------------------------------------------------------")
print(paragraph)
print("----------------------------------------------------------------------\n")

print('"un" appears in the text', num_un, 'time(s) and the lowest index of the first occournce of "un" is at index', index_un)
print('"an" appears in the text', num_an, 'time(s) and the lowest index of the first occournce of "on" is at index', index_an)
print('"in" appears in the text', num_in, 'time(s)and the lowest index of the first occournce of "on" is at index', index_in)
print('"he" appears in the text', num_he, 'time(s) and the lowest index of the first occournce of "on" is at index', index_he)
