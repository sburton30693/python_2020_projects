# Spencer Burton
# 9/21/20
# Chapter 3.2 Getting Input

# Always assign input to a variable
user_name   = input("What is your legal name? ")
user_age    = int(input("What is your age? "))
user_grade  = int(input("What grade are you in? "))
user_retire = int(input("What age do you want to retire at? "))

years_until_21 = 21 - user_age
graduation = 12 - user_grade
years_until_ret = user_retire - user_age

print()
print("You turn 21 in", years_until_21, "year(s)")
print("You graduate in", graduation, "year(s)")
print("You will retire in", years_until_ret, "year(s)")
