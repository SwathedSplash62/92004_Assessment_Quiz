import math
import random


def round_check(question):
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


def int_check(question, low=None, exit_code=None, high=None):
    # if any integer is allowed. . .

    if low is None and high is None:
        error = "Please enter an integer"

    # if the number needs to be more than an integer (ie: rounds / high number)
    elif low is not None and high is None:
        error = f"Please enter an integer that is more than / equal to {low}"

    # if the number needs to between low & high
    else:
        error = f"Please enter an integer that is between {low} and {high} inclusive"

    while True:
        response = input(question).lower()

        try:

            if response == exit_code:
                return response

            response = int(response)

            # if too low
            if low is not None and response < low:
                print(error)

            # is more than low num
            elif high is not None and response > high:
                print(error)

            # if valid then return
            else:
                return response

        except ValueError:
            print(error)


def statement_generator(text, decoration):
    # Make string with five characters
    ends = decoration * 2

    # add decoration to start and end of statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


def instructions():
    statement_generator("Instructions/information", "-")
    print('''
To begin, choose the number of rounds (or press <enter> for infinite mode).

You will then chose a lower and higher number (inclusive) that will contain your secret number 

You will then try to guess the number while the computer will give you hints for each guess

You will receive statistics on your guesses used and will be able to see your game history at the end of the game 

Type <quit> to end the game at anytime.

🎂🎂🎂Good Luck🎂🎂🎂
''')
    print()
    return ""


def calc_guesses(low, high):
    num_range = high - low + 1
    max_raw = math.log2(num_range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    return max_guesses


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
# Title
statement_generator("Higher Lower", "👆👇")

# instructions
want_instructions = string_checker("Do you want to see the instructions?", yes_no_list)
if want_instructions == "yes":
    instructions()

# Ask user for number of rounds
num_rounds = round_check("How many rounds would you like? Push <enter> for ⌚️infinite mode⌚️: ")

if num_rounds == "":
    mode = "infinite"
    num_rounds = 5