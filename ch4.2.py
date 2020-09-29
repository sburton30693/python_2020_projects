# Spencer Burton
# 9/29/20
# Chapter 4 Lesson 2

##x = "a"
##a = "A"
##
##if x >= a :
##    print("greater than")
##
##    # Nested if statement
####    if a > 5 :
####        print("testing")
##
##if x <= a :
##    print("less than")
##
##print("Back to main branch")



score = "a word"

# Logical expressions can be wrapped with parentheses
# elif - If the first one is not true check the next one
if (score >= 90) :
    print("That's better!")

elif (score >= 80) :
    print("Looking great")

elif (score >= 70) :
    print("You rock!")
    
elif (score >= 60) :
    print("Try harder")

# else - The catch all, if none above evaluate to true, else will run
else :
    print("You failed")
