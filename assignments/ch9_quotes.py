import random

# define a function that returns a random quote
def select_quote() :

    # set up a tuple of available quotes
    quotes = ("My fake plants died because I did not pretend to water them - Mitch Hedberg", \
            "There cannot be a crisis next week.  My schedule is already full. - Henry Kissinger", \
            "Weather forecast for tonight: dark. - George Carlin", \
            "All generalizations are false, including this one. - Mark Twain", \
            "Why do they call it rush hour when nothing moves? - Robin Williams")



    # get the number of available quotes
    numQuotes = len(quotes)

    # get a random number between 0 and numQuotes - 1 (the last valid tuple index)
    index = random.randrange(0, numQuotes - 1)

    # print the selected quote
    print(quotes[index])
  
    # function is complete
    return

# main program will call select_quote() twice
select_quote()
select_quote()
