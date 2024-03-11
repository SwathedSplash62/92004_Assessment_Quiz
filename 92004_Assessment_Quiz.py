import math
import random
from turtle import clear


# This checks for the answers to be actual valid integers
def num_checker(question, exit_code=None):
    valid = False
    while not valid:
        error = "Please enter an integer that is 1 or more"

        while True:
            to_check = input(question).lower()

            if to_check == "":
                return ""

            try:

                if to_check == exit_code:
                    return to_check

                # ask user to enter a number
                response = int(to_check)

                # checks number is more than one
                if response < 1:
                    print(error)

                elif to_check == "":
                    return ""
                # Outputs error if input is invalid
                else:
                    return response

            except ValueError:
                print(error)


# used for simple commands - yes_no - and is easy to implement
def string_checker(question, valid_ans):
    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        user_response = input(question).lower()

        for item in valid_ans:
            if item == user_response:
                return item

            elif user_response == item[0]:
                return item

        # print error when error
        print(error)
        print()


# makes big centered headings
def statement_generator(text, decoration):
    # Make string with five characters
    ends = decoration * 2

    # add decoration to start and end of statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


# contains instructions for instructing
def instructions():
    statement_generator("Instructions/information", "-")
    print('''
To begin, choose the number of rounds (or press <enter> for infinite mode).

You will receive questions about the area of different shapes, the units will be automatically accounted for; e.g you 
will not have to enter them 

Type: "quit" to exit the game at anytime 
 
🐥🐥🐥Good Luck🐥🐥🐥
''')
    print()
    return ""


# Main routine goes here

# what the game is supposed to be
correct_answers = []
total_questions = []
mode = "regular"
rounds_played = 0
feedback = ""
end_game = "no"
guess = 0
yes_no_list = ['yes', 'no']
game_history = []
all_scores = []
value_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ]
# Title
statement_generator("Super duper hard math test", "🤖💎")
# instructions
want_instructions = string_checker("Do you want to see the instructions?", yes_no_list)
if want_instructions == "yes":
    instructions()

# how many questions they would like to be asked of them?
num_rounds = num_checker("How many rounds would you like? Push <enter> for 🎊🎊infinite mode🎊🎊: ")

if num_rounds == "":
    mode = "infinite"
    num_rounds = 5

while rounds_played < num_rounds:

    # creates infinite
    if mode == "infinite":
        num_rounds += 1

    # rounds based on mode
    if mode == "infinite":
        rounds_heading = f"\n🐂🐂🐂 Round {rounds_played + 1} (Infinite Mode) 🐂🐂🐂"
    else:
        rounds_heading = f"\n🍙🍙🍙 Round {rounds_played + 1} of {num_rounds} 🍙🍙🍙"

    print(rounds_heading)

    width = random.choice(value_list)
    length = random.choice(value_list)
    if length == width:
        shape = "square"
    else:
        shape = "rectangle"

    question = num_checker(f"What is the area of this {shape} if the width is {width}m and length is"
                           f" {length}m? ", exit_code="quit")

    if question == "quit":
        end_game = "yes"
        break
    answer = width * length
    print(f"You chose {question}m")
    print(f"The answer was {answer}m")

    if question == answer:
        result = print("Congrats you are right")
        rounds_played += 1
        correct_answers.append(result)
    else:
        result = print("You are wrong")
        rounds_played += 1
        total_questions.append(result)


if rounds_played > 0:

    # Behold, stats

    # Output stats
    print("📈📈📈 Game Statistics 📈📈📈")
    print(
        f"Best: {correct_answers} out of {total_questions}")
    print()

    see_history = string_checker("Do you want to see your game history? ", yes_no_list)
    if see_history == "yes":
        for item in game_history:
            print(item)

else:
    "..."

# final statement before game end

print("   Thank you for playing")
statement_generator("Super duper hard math test", "🤖💎")
print()