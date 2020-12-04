# Spencer Burton
# 12/4/2020
# Mr. Roboto

class Robot :
    
    def __init__(self) :
        self.name = "Mr. Roboto"
        self.thankYou = "Domo arigato"
        
    def thanks(self) :
        print(self.thankYou + ", " + self.name)
        
        
def main() :
    robot = Robot()
    robot.thanks()
    
    robot.thankYou = "Thankee Kindly"
    robot.name = "T-1000"
    robot.thanks()
    
main()