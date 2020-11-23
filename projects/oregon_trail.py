# James Hooper and Spencer Burton

import datetime
import random

#**********************************Functions**************************************************************
def logo_screen() :
    """This is the first screen"""

    logo = \
"""
-----        _____ _                      __          __      _            
|    \      / ____| |                     \ \        / /     | |           
|     \    | |    | |__   ___  ___  ___  __\ \  /\  / /__  __| | __ _  ___ 
|      \   | |    | '_ \ / _ \/ _ \/ __|/ _ \ \/  \/ / _ \/ _` |/ _` |/ _ \\
|       \  | |____| | | |  __/  __/\__ \  __/\  /\  /  __/ (_| | (_| |  __/
----------  \_____|_| |_|\___|\___||___/\___| \/  \/ \___|\__,_|\__, |\___|
            Studios                                              __/ |     
                                                                |___/   
                                Presents                               
                           - The Oregon Trail -
"""
    
    names = "James Hooper and Spencer Burton"
    copy_right = "Copyright (c) 2020"

    print(str.format("{} {}\n {}", copy_right, names, logo))

    input("\nPress Enter to stop appreciating our art")

def menu(options) :
    value = ""
    success = False

    print("You may:")

    for i in range(len(options)) :
        print(str.format("  {}. {}", i + 1, options[i]))

    value = get_number("What do you choose: ", 1, len(options))

    return value


def start_screen() :

    oregon_trail = \
"""
_______________________________________________________________________________
  _______ _             ____                               _______        _ _ 
 |__   __| |           / __ \                             |__   __|      (_) |
    | |  | |__   ___  | |  | |_ __ ___  __ _  ___  _ __      | |_ __ __ _ _| |
    | |  | '_ \ / _ \ | |  | | '__/ _ \/ _` |/ _ \| '_ \     | | '__/ _` | | |
    | |  | | | |  __/ | |__| | | |  __/ (_| | (_) | | | |    | | | | (_| | | |
    |_|  |_| |_|\___|  \____/|_|  \___|\__, |\___/|_| |_|    |_|_|  \__,_|_|_|
                                        __/ |                                 
                                       |___/                                   
"""

    print(oregon_trail)

    finished = False

    while not finished :
        choice = menu(["Start Game", "Learn about the Trail", "End"])

        if choice == 1 :
            # Start game
            play_game()
            finished = True
        elif choice == 2 : # Tell about game
            learn()

            input("Press Enter to continue")
        else :
            finished = True

        # For spacing
        if not finished :
            print()

def learn() :
    """This is Used when the learn of trail is chosen"""
    print("""\nTry taking a journey by covered wagon across 2000 miles of plains, rivers, and mountains. Try! On the plains,
will you slosh your oxen through mucd and water-filled ruts or will you plod through dust six inches deep?\n""")
    input("Press Enter To Continue")
    print("""\nHow will you cross the rivers? If you have money, you might take a ferry (if there is a ferry).
Or, you can ford the river and hope you and your wagon aren't swallowed alive!\n""")
    input("Press Enter To Continue")
    print("""\nWhat about supplies? Well, if you're low on food you can hunt. You might get a buffalo... you might.
And there are bear in the mountains.\n""")
    input("Press Enter To Continue")
    print("""\nAt the Dalles, you can try navigating the Columbia River, but if running the rapids with a makeshift
raft makes you queasy, better take the Barlow Road.\n""")
    input("Press Enter To Continue")
    print("""\nIf for some reason you don't survive -- your wagon burns or thieves steal your oxen,
or you run out of provisisons, or you die of cholera -- don't give up! Try again... and again...\n""")
    input("Press Enter To Continue")
    print("\nThe software team responsible for creation of this product includes:\n - Spencer Burton\n - James Hooper\n")

def month_advice() :
    """Prints the text when you ask for advice"""
    print("""
You attend a public meeting held for “folks with the California - Oregon fever.” You are told:

If you leave too early, there won’t be any grass for your oxen to eat. If you leave too late,
you might not get to Oregon before winter comes. If you leave at just the right time,
there will be green grass and the weather will still be cool.""")
    input("\nPress Enter To Continue")


def play_game() :
    """The actual game function"""

    # Get profession and money that profession has
    prof_data = char_setup()
    profession = prof_data[0]
    money = prof_data[1]
    
    # Name Leader and other members
    members = name_members()

    # Choose month
    month = 0
    
    while True :
        print("\nIt is 1848. Your jumping off place for Oregon is Independence,\n\
Missouri. You must decide which month to leave Independence.")
        choice = menu(["March", "April", "May", "June", "July", "Ask for advice"])

        if choice == 6 :
            month_advice()
        else :
            month = choice
            break

    # Defern sum veriables
    START_DATE = datetime.datetime(1848, month + 2, 1)
    current_date = START_DATE
    hp = 100
    ox_hp = 100
    total_miles = 2000
    miles_traveled = 0

    # Declare variables for shop
    food = 0
    ammo = 0
    clothes = 0
    parts = []
    oxen = 0
    
    shop_data = shop(money, food, ammo, clothes, parts, oxen)
    money = shop_data[0]
    food = shop_data[1]
    ammo = shop_data[2]
    clothes = shop_data[3]
    parts = shop_data[4]
    oxen = shop_data[5]

    # Choose weather based on month
    weather = ("cool", "cool", "good", "good", "hot")[month - 1]
    health = "good"
    pace = "normal"
    rations = "filling"

    
    while len(members) > 0 and miles_traveled < total_miles and oxen > 0:
        turn_data = turn(weather, hp, health, rations, current_date, members, food, oxen, miles_traveled, total_miles, money, pace, ammo, clothes, parts)
        weather = turn_data[0]
        hp = turn_data[1]
        health = turn_data[2]
        rations = turn_data[3]
        current_date = turn_data[4]
        food = turn_data[5]
        oxen = turn_data[6]
        miles_traveled = turn_data[7]
        pace = turn_data[8]
        ammo = turn_data[9]
        clothes = turn_data[10]
        parts = turn_data[11]
        members = turn_data[12]

    if miles_traveled >= total_miles :
        print("Congrats on getting to Oregon")
        input("Press enter to exit")
    elif len(members) <= 0:
        print("Looks you like all your members died, too bad")
        input("Press enter to exit")
    else :
        print("Looks you like all your oxen are gone, too bad")
        input("Press enter to exit")
        

def turn(weather, hp, health, rations, current_date, family, food, oxen, miles_traveled, total_miles, money, pace, ammo, clothes, parts) :
    weather = random.choice(("hot", "good", "fair", "poor", "windy", "rain", "blizzard"))

    if hp >= 80 :
        health = "good"
    elif hp < 80 and hp >= 50 :
        health = "fair"
    else :
        health = "poor"

    if rations == "filling" :
        rations_mod = 2
    elif rations == "meager" :
        rations_mod = 1
    else :
        rations_mod = 0.5

    problem = random.choice(("lost", "snake bite", "sick", "rip ox", "none", "none", "none",
                             "none", "none", "none", "none"))

    rand_person = random.choice(family)
    problem_string = ""
    
    if problem == "lost" :
        lost = random.randint(1, 7)
        problem_string = rand_person + " got lost for " + str(lost) + " days"
        current_date += datetime.timedelta(days = lost)
        if food >= (len(family) - 1) * rations_mod * lost :
            food -= (len(family) - 1) * rations_mod * lost
        else :
            hp -= 10
    elif problem == "snake bite" :
        problem_string = rand_person + " got bitten by a snake"
        hp -= 50
    elif problem == "sick" :
        problem_string = rand_person + random.choice([" got dysentary", " got cholera", " got covid-47", " broke their arm",
                                                    " ate a random mushroom"])
        hp -= 20
    elif problem == "rip ox" :
        problem_string = random.choice(("One of your ox has died, but you got some more food because of it",
                             "A thief left a note saying 'I stole one of your oxen, but I felt bad and left some food'"))
        oxen -= 1
        food += 50


    # Check if someone died
    if hp <= 0 :
        family.remove(rand_person)
        hp = 100
        print(rand_person, "has died\n")

    print(str.format("""\n
   .....                                        ..'..                              ..',,,'..        
..',;;;,,'...  ...                       ..'''',,;;;;,..                       ..',;;;;;;;;,,,'..   
,;;,;;;;;,;;;,,,;,,...               ..',;;;;;,,;;;;;;;;,'..     ..''....',,'',,;;;;;;;;;;,;;;;;,'..
;;;;;;;;;;;;;;;;;;;;;,,....'..   ..',;;;;;;;;;;;;;;;;;;;;;;,'..',;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,,',,;,,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
''''''''''''''',,,''''.........'''''',,,''''''''''''',,;;;;;,,,,,,,,,,,,;;;;;;;;;;;;,,,''...'',,,;;;
                                                      ........        ...............            ...
 +-----------------------------+                                                                    
 |Date:{:_>24}|                 
 |Weather:{:_>21}|           ..'''''''''''..                         ..''''''.        
 |Health:{:_>22}|          ,:ccccllllllllc::::,...  ......  ..,::::::clclllcc,.      
 |Miles Traveled:{:_>14}|         .cc'.;cccclccccccccclc'.;cllllc;.'ccccccccccccclcl;.      
 |Miles To Go:{:_>17}|          .;c, .,:clcclclcclcclc'.clcccclc.'cccccccccccclll:.       
 |Food:{:_>24}|           .cc.  .';cccclcclcclc'.clcccclc.'cccccccccccccc:.        
 +-----------------------------+            ,:;.   'ccccccclcclc'.clcccclc.'cccccccccccccc'         
                 ..                         .;c;.   ,ccclccccllc'.clcccllc.'cccccclccllcc,          
          .,,. .'::.  ....                   .:c.   .clcccccclcc'.cccccclc.'cccccccccccc'           
           .,:::cl,..',';c;:;;;;:;;;'.        ',.   .:cccccccccc..:cccccc:.'ccccccccccc:.           
         .';clcccl,';;::ccccccccccccc:.       ....  ......,,,,'.  .............',,,,..','.          
          ...';:;,,;cccllcclcclccccccc........'.''.',...',.,;',,. .,','',,,  .,'';,','.''.          
                .;:clcclcccclllccccc:,.      ...',... .,'. ', .';. ..,',,.. .;. .,. .,,.            
                 .'clcccc::;'.,:lclc.         ..''    ';...;;...;'   ''''   ,;..';,..';.            
                  .cc,:c;..  .,cc,:c.                 .,'. ', .',.          .;. .,. .,,.            
                .':c,..;l'   .';:;:c.                  .',',;','.            .,,';,',.              
'..''.''''.'''.',:c:,'';:,''''',::::,'''''...'''''''''''',;;;;,''''''''''..'''';;;;;,'''.''''''''''.
;;;;;;;;;;;;;;,;;:::;;;::;,,;;;;::;;;;;;;;;;;;;;;;;;;;;;;;;;;,;;;;;;;;;;;;;;;;;;,;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;,;::::;;;:;;;;;;;:::;;;;;;;;;;;;;;;;;;;;;;;;;,;;,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,
;;{:;<87};;;;;;;;;;;
""",current_date.strftime("%A %b %d, %Y"),weather,health,miles_traveled,total_miles - miles_traveled,food, problem_string))

    while True :
        choice = menu(("Continue on trail", "Check supplies", "Change pace", "Change food ration",
                       "Stop to rest", "Attempt to trade", "Hunt for food"))

        print()
        
        if choice == 1 :
            # Continue on trail
            miles_traveled += travel(weather, pace, health, oxen)
            if food >= len(family) * rations_mod :
                food -= len(family) * rations_mod
            else :
                hp -= 10
            current_date += datetime.timedelta(days = 1)
            break
            
        elif choice == 2 :
            # Check Supplies
            check_supplies(money, food, ammo, clothes, oxen, parts)

        elif choice == 3 :
            # Change Pace
            pace = change_pace(pace)

        elif choice == 4 :
            # Change food ration
            rations = change_rations(rations)
                
        elif choice == 5 :
            # Rest
            hp, rest_days = rest(hp, health)
            if food >= len(family) * rations_mod * rest_days :
                food -= len(family) * rations_mod * rest_days
            else :
                hp -= 10
            current_date += datetime.timedelta(days = rest_days)
        
        elif choice == 6 :
            # Attempt to trade
            print("There was no one to trade with")
            
        elif choice == 7  and ammo > 0:
            # hunt
            hunt_data = hunt(ammo, food)
            ammo = hunt_data[0]
            food = hunt_data[1]
            if food >= len(family) * rations_mod * hunt_data[2] :
                food -= len(family) * rations_mod * hunt_data[2]
            else :
                hp -= 10
            current_date += datetime.timedelta(days = hunt_data[2])

        print()

    # Make sure food not less than zero
    if food < 0 :
        food = 0

    return (weather, hp, health, rations, current_date, food, oxen, miles_traveled, pace, ammo, clothes, parts, family)
    

def char_setup() :
    """Gets the profession and returns it and the amount of money they have"""

    print("\nMany kinds of people made the trip to Oregon.\n")

    description = """
Traveling to Oregon isn't easy! But if you're a banker, you'll have more
money for supplies and sevices than a carpenter or a farmer.

However, the harder you have to try, the more points you deserve! Therefore, the farmer
earns the greatest number of points and the banker earns the least.

 - Banker   : $1600.00
 - Carpeter : $800.00
 - Farmer   : $400.00\n"""

    profession = ""
    money = 0

    while True :

        choice = menu(("Be a banker from Boston", "Be a carpenter from Ohio", "Be a farmer from Illinois", "Find out the differences"))

        if choice == 1 :
            # Banker
            profession = "banker"
            money = 1600
            break
        elif choice == 2 :
            # Carpenter
            profession = "carpenter"
            money = 800
            break
        elif choice == 3 :
            # Farmer
            profession = "farmer"
            money = 400
            break
        elif choice == 4 :
            print(description)
            input("Press Enter To Continue")
            print()

    return (profession, money)

def name_members() :
    """Get the names of wagon leader and family members"""
    leader_name = get_name("\nWhat is the name of your wagon leader? ")

    # Ask how many family members
    print()
    num_family = get_number("How many other family members? ", 1, 9)

    family_names = [leader_name]

    # Get names of family members
    print()
    
    for i in range(num_family) :
        family_names.append(get_name(str.format("What is the name of member #{}? ", i + 1)))

    # Maybe Later : Ask if they are sure, if not get number in range of the names and change it with get_name

    return family_names

def get_name(question) :
    """Get name that is valid"""
    while True :
        name = input(question)

        if len(name) >= 2 and len(name) <= 16 :
            return name

def get_number(question, min, max) :
    """Gets number in range"""
    while True :
        valid = True
        
        number = input(question)

        # Make sure it is only numerical digits
        for digit in number :
            if not digit in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9") :
                valid = False

        if valid and not number == "" :
            num = int(number)

            if num >= min and num <= max :
                return num
    
def shop(money,food,ammo,clothes,wagon_parts,oxen) :
    """Handles the shopping interface"""
    bill = 0
    inventory = []
    items = ["Oxen","Food","Ammo","Clothing","Wagon Parts","Check Out"]
    spent_on_items = [0.00,0.00,0.00,0.00,0.00,bill]

    print("\nBefore leaving Indipendance you should buy equipment and supplies.")
    print(str.format("You have ${} in cash, but you don't have to spend it all now", money))
    print("You can buy whatever you need at Matt's General Store.")
    input("\nPress Enter To Continue")

    while True :
        # Update bill in the list
        spent_on_items[len(spent_on_items) - 1] = bill

        print("\nWelcome to Matt's General Store")
        print("Here is a list of things you can buy")

        # Display current money and choices
        for i in range (len(items)):
            print(str.format("{}. {:20} ${:.2f}", i + 1, items[i], spent_on_items[i]))
        print(str.format("Total Bill so far:      ${:.2f}", bill))
        print(str.format("Total funds available:  ${:.2f}\n", money - bill))

        choice = get_number("What item would you like to buy: ", 1, len(items))

        # Oxen buying
        if choice == 1 :
            # Subtract any previous money from this from the bill
            bill -= spent_on_items[0]
            oxen = 0
            spent_on_items[0] = 0
            
            print("\nThere are 2 oxen in a yoke; \nI recommend at least 3 yoke. \nI charge $40.00 a yoke.\n")
            print(str.format("Total Bill so far:      ${:.2f}", bill))
            num_yoke = get_number("How many yoke do you want: ", 1, 5)

            cost = num_yoke * 40
            oxen = num_yoke * 2
            bill += cost
            spent_on_items[0] = cost

        # Food buying
        elif choice == 2 :
            # Subtract any previous money from this from the bill
            bill -= spent_on_items[1]
            food = 0
            spent_on_items[1] = 0
            
            print("""
I recommend you take at least 200 pounds of food
for each person in you family.
I Charge $0.20 a pound.\n""")
            print(str.format("Total Bill so far:      ${:.2f}", bill))
            food = get_number("How many pounds of food do you want: ", 1, 2500)

            cost = food * 0.2
            bill += cost
            spent_on_items[1] = cost

        # Ammo buying
        elif choice == 3 :
            # Subtract any previous money from this from the bill
            bill -= spent_on_items[2]
            ammo = 0
            spent_on_items[2] = 0
            
            print("\nI sell ammunition in boxes of 20 bullets each box costs $2.00\n")
            print(str.format("Total Bill so far:      ${:.2f}", bill))
            num_boxes = get_number("How many boxes do you want: ", 1, 99)

            cost = num_boxes * 2
            ammo = num_boxes * 20
            bill += cost
            spent_on_items[2] = cost

        # Clothes buying
        elif choice == 4 :
            # Subtract any previous money from this from the bill
            bill -= spent_on_items[3]
            clothes = 0
            spent_on_items[3] = 0
            
            print("""
You'll need warm clothing in the mountains.
I recommend taking at 2 sets of clothing per person.
Each set is $10.00.\n""")
            print(str.format("Total Bill so far:      ${:.2f}", bill))
            clothes = get_number("How many sets of clothes do you want: ", 1, 40)

            cost = clothes * 10
            bill += cost
            spent_on_items[3] = cost

        # Parts buying
        elif choice == 5 :
            # Subtract any previous money from this from the bill
            bill -= spent_on_items[4]
            spent_on_items[4] = 0
            parts_bill = 0
            inventory = []
            parts = ["Wagon Wheel", "Wagon Axle", "Wagon Tongue", "back to main shop"]
            parts_cost = [10.00, 20.00, 50.00, parts_bill]

            print("\nIt's a good idea to have a few spare parts for your wagon\n")

            while True :
                parts_cost[len(parts_cost) - 1] = parts_bill
                print("\nHere is a list of things you can buy:")
                for i in range(len(parts)) :
                    print(str.format("{}. {:20} ${:.2f}", i + 1, parts[i], parts_cost[i]))
                print(str.format("Total Bill so far:      ${:.2f}", bill + parts_bill))
                print(str.format("Total funds available:  ${:.2f}\n", money - (bill + parts_bill)))
                item = get_number("What item would you like to buy: ", 1, len(parts))

                if item == 1 :
                    wheels = get_number("How many Wagon Wheels do you want: ", 0, 3)
                    for i in range(wheels) :
                        inventory.append("Wagon Wheel")
                    parts_bill += parts_cost[0] * wheels

                elif item == 2 :
                    axles = get_number("How many Wagon Axles do you want: ", 0, 3)
                    for i in range(axles) :
                        inventory.append("Wagon Axle")
                    parts_bill += parts_cost[1] * axles

                elif item == 3 :
                    tongues = get_number("How many Wagon Tongues do you want: ", 0, 3)
                    for i in range(tongues) :
                        inventory.append("Wagon Tongue")
                    parts_bill += parts_cost[2] * tongues

                elif item == 4 :
                    bill += parts_bill
                    spent_on_items[4] = parts_bill
                    break

        # Check out
        elif choice == 6 :
            if (money - bill) < 0 :
                print("\nYour bill exceeds your balance, please remove some items")
            else :
                return (money - bill, food, ammo, clothes, wagon_parts + inventory, oxen)

def change_rations(rations):
    """Displays Current rations then lets you change it"""
    print("Current Rations:",rations)
    choice = menu(("filling","meager","bare bones"))
    if choice == 1:
        rations = "filling"
    elif choice == 2:
        rations = "meager"
    elif choice == 3:
        rations = "bare bones"
    return rations

def change_pace(pace):
    """Displays Current pace then lets you change it"""
    print("Current Pace:",pace)
    choice = menu(("fast","normal","slow"))
    if choice == 1:
        pace = "fast"
    elif choice == 2:
        pace = "normal"
    elif choice == 3:
        pace = "slow"
    return pace

def check_supplies(money, food, ammo, clothes, oxen, parts) :
    """Displays current supplies"""
    print("Money:", "$" + str(money))
    print("Food:", food)
    print("Ammo:", ammo)
    print("Clothes:", clothes)
    print("Oxen:", oxen)
    print("Parts:", parts)

def travel(weather, pace, health, oxen) :
    """Travels a certain number of miles based on weather, pace, and health"""
    mph = 0
    hours = 0
    weather_mod = 0

    # Determine hours per day
    if health == "good" :
        hours = 8
    elif health == "fair" :
        hours = 4
    elif health == "poor" :
        hours = 2

    # Determine miles per hour
    if pace == "slow" :
        mph = 1
    elif pace == "normal" :
        mph = 2
    elif pace == "fast" :
        mph = 4

    # Determine weather modifier
    if weather == "rain" :
        weather_mod = 0.5
    elif weather == "hot" :
        weather_mod = 0.25
    elif weather == "blizzard" :
        weather_mod = 0
    else :
        weather_mod = 1

    # Do the calculuminations
    miles = mph * hours * weather_mod * (oxen // 2)

    return miles

def hunt(ammo, food):
    if ammo > 10 :
        used_ammo = random.randint(1, 10)
    else :
        used_ammo = random.randint(1, ammo)

    ammo -= used_ammo
    added_food = random.randint(50, 200)
    food += added_food
    days = random.randint(0, 3)
    print("You went hunting and got", added_food, "lbs of food and used", used_ammo, "bullets, after", days, "days.")

    return (ammo, food, days)

def rest(health,rations):
    days = get_number("How many days do you want to rest ", 0, 9)
    if rations == "filling":
        health_mod = 2
    elif rations == "meager":
        health_mod = 1
    else :
        health_mod = .5
        
    health_gain = 10 * days * health_mod
    if (health_gain + health) > 100:
        health = 100
    else:
        health += health_gain
        
    return health, days


    
#***********************************************************************************************************

# Display splash screen
logo_screen()

# Display start menu and start the game
start_screen()
