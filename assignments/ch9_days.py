import datetime

# define the get_day_of_week() function here
def get_day_of_week(target) :
    try :
        thisDate = datetime.datetime.strptime(target, "%Y-%m-%d")
        dayOfWeek = datetime.datetime.strftime(thisDate, "%A")
        return dayOfWeek

    except :
        return "Invalid YYYY-MM-DD Date"


# main code starts here
print(get_day_of_week("1776-07-04"))  # US Declaration of Independence adopted
print(get_day_of_week("1918-11-11"))  # World War I Armistice Day
print(get_day_of_week("3-16-2001"))   # Test invalid date format
