# Spencer Burton
# Did you pass?

myGrade = 95
myLetterGrade = "Not Assigned"

if myGrade > 90:        # myGrade is greater than or equal to 90
    myLetterGrade = "A"
elif myGrade > 80:      # myGrade is greater than or equal to 80
    myLetterGrade = "B"
elif myGrade > 70 :
    myLetterGrade = "C" #add more elif and else statements here to handle C, D and F
elif myGrade > 60 :
    myLetterGrade = "D"
else :
    myLetterGrade = "F"

#print out the grade
print("My grade is:", myLetterGrade)
