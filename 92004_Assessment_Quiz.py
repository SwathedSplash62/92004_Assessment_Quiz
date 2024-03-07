import math
import random


# This checks for the answers to be actual valid integers
def num_checker(question):
    valid = False
    while not valid:
        error = "Please enter an integer that is 1 or more"

        to_check = input(question)

        if to_check == "":
            return ""

        try:

            # ask user to enter a number
            response = int(to_check)

            # checks number is more than one
            if response < 1:
                print(error)
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

You will then chose a lower and higher number (inclusive) that will contain your secret number 

You will then try to guess the number while the computer will give you hints for each guess

You will receive statistics on your guesses used and will be able to see your game history at the end of the game 

Type <quit> to end the game at anytime.

🐥🐥🐥Good Luck🐥🐥🐥
''')
    print()
    return ""


# Main routine goes here

# what the game is supposed to be
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

    # rounds based on mode
    if mode == "infinite":
        rounds_heading = f"\n🐂🐂🐂 Round {rounds_played + 1} (Infinite Mode) 🐂🐂🐂"
    else:
        rounds_heading = f"\n🍙🍙🍙 Round {rounds_played + 1} of {num_rounds} 🍙🍙🍙"
    
    width = random.choice(value_list)
    length = random.choice(value_list)
    if guess f"{width} == {length}:
        shape = "square"

        question = num_checker(f"The area of a {shape}: ", )



