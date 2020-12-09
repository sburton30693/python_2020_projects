# Spencer Burton
# 12/3/2020
# Trivia Program

# Imports
import sys
from datetime import datetime

# Functions

def open_file(file_name, mode) :
    """Open and return an open file with the given permissions"""
    try :
        file = open("assets/test_files/" + file_name, mode)
    except IOError as e :
        print("Unable to open the file", file_name, "Ending program.\n", e)
        try :
            file = open("assets/errors/errors_log.txt", "a+")
            time = datetime.now()
            error_time = time.strftime("%m/%d/%Y %H:%M:%S")
            file.write(str(error_time) + " " + str(e) + "\n")
            input("\nPress enter to exit.")
            sys.exit()
        except :
            sys.exit()
    else :
        return file

def next_line(file) :
    try :
        line = file.readline()
        line = line.replace("/", "\n")
        return line
    except :
        print("Could not read line")
        sys.exit()

def next_question(file) :
    """Return the next question block of data from the trivia file."""
    category = next_line(file)
    question = next_line(file)
    answers = []

    for i in range(4) :
        answers.append(next_line(file))

    correct = next_line(file)
    if correct :
        correct = correct[0]

    explanation = next_line(file)

    return category, question, answers, correct, explanation

def get_name() :
    name = ""

    try :
        while True :
            name = input("What is your name? ")
        
            if (len(name) >= 3) and (" " in name) :
                time = datetime.now()
                test_time = time.strftime("%m/%d %H:%M")
                return name.title(), test_time
    except :
        print("An error occured while getting name")
        sys.exit()

def welcome(title, name, test_time) :
    """Welcome the player."""
    print("Welcome", name, "to your Mid Term\n")
    print("Your test is", title)

def create_report_card(name, test_time, score, total_questions) :
    print("Writing report card...")
    
    card = open_file(name.replace(" ", "_") + ".txt", "w")
    card.write("Name = " + name + "\n")
    card.write("# Correct = " + str(score) + "\n")
    percentage = (score / total_questions) * 100
    card.write("% Correct = %" + str(percentage) + "\n")
    card.write("Letter Grade = ")

    if percentage >= 90.0 :
        card.write("A")
    elif percentage >= 80.0 :
        card.write("B")
    elif percentage >= 70.0 :
        card.write("C")
    elif percentage >= 60.0 :
        card.write("D")
    else :
        card.write("F")

    card.close()

    print("Report card written.")

def main() :
    # Will need to change file name to match test your taking
    file = open_file("sb_test.txt", "r")
    title = next_line(file)
    name, test_time = get_name()
    welcome(title, name, test_time)
    score = 0
    total_questions = 0

    category, question, answers, correct, explanation = next_question(file)

    while category :
        total_questions += 1

        print(category)
        print(question)

        for i in range(len(answers)) :
            print(str.format("\t{}: {}", i + 1, answers[i]))

        # Get answer
        answer = input("What is your answer? ")

        # Check answer
        if answer == correct :
            print("\nRight!", end = " ")
            score += 1
        else :
            print("\nWrong.", end = " ")

        print(explanation)
        print("Score:", score, "\n\n")

        category, question, answers, correct, explanation = next_question(file)

    file.close()
    print("That was the last question!")
    print("Your final score is:", score)
    create_report_card(name, test_time, score, total_questions)

main()
