# Spencer Burton
# 10/2/20
# Blue Moon

# Get input from user
blue_moon = input("Is there a blue moon tonight(Yes / No)? ")
week_day = input("What is the day of the week(Monday - Sunday)? ")
month_day = int(input("What is the day of the month(1 - 31)? "))

song = "Day Dream Believer"

# Check for conditions

if blue_moon == "Yes" or blue_moon == "yes" :
    song = "Once in a Blue Moon"

elif month_day <= 7 :
    if week_day == "Monday" or week_day == "monday" :
        song = "Manic Monday"
    elif week_day == "Tuesday" or week_day == "tuesday" :
        song = "Tuesday Gone"
    elif week_day == "Wednesday" or week_day == "wednesday" :
        song = "Just Wednesday"
    elif week_day == "Thursday" or week_day == "thursday" :
        song = "Sweet Thursday"
    elif week_day == "Friday" or week_day == "friday" :
        song = "Friday I'm in Love" 
    elif week_day == "Saturday" or week_day == "saturday" :
        song = "Saturday at the Park"
    elif week_day == "Sunday" or week_day == "sunday" :
        song = "Lazing on a Sunday Afternoon"
    else :
        song = "Days of the Week"


# Display Song to User
print("Play song '" + song + "'")
