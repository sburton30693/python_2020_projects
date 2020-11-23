# Spencer Burton

import datetime

# Define the get_verified_integer function
def get_verified_integer(prompt, min, max) :
    while True :
        try :
            answer = int(input(prompt))
            
            if (answer >= min) and (answer <= max) :
                return answer
            else :
                print("Try again - ", end = "")
        except :
            print("Try again - ", end = "")
            


# main program starts here
month = get_verified_integer("Please enter today's month (1-12): ",1,12)
day   = get_verified_integer("Please enter today's day (1-31): ",1,31)
year  = get_verified_integer("Please enter today's year (2000 - 2030): ",2000,2030)

# build date object and print out the day of the week
today = datetime.date(year,month,day)
print("Today is a " + today.strftime("%A"))
