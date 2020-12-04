# Spencer Burton
# 12/4/2020
# 10.3 Best Friends Bestie class

class Bestie :
    numMessages = 0

    def chat(self, input) :
        Bestie.numMessages += 1

        if Bestie.numMessages > 3 :
            print("I'm too tired")
            return

        input = str.lower(input)

        if "ride" in input :
            print("Sure I'll give you a ride")
        elif "call" in input :
            print("I'll call you later")
        else :
            print("You are a mystery to me")
