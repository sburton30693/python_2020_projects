# Spencer Burton
# 9/25/20
# Chapter 4 Logic

# True and False must be capitalized
is_awake = True
is_sleeping = False

# comparison
result = 30 < 555 # True
print(result)

input_1 = input("Enter a number between 1 and 100 ")
input_2 = input("Enter another number between 1 and 100 ")

result = input_1 == input_2
print("Is input equal to input two:", result)

# Comparison operators > < >= <= == !=

# if statements (flow control)
if input_1 != input_2 :
    print("input_1 != input_2")


password = "Password1!"

user_input = input("Enter your password: ")

if user_input == password :
    print("Correct password")

if user_input != password :
    print("Invalid Password")
