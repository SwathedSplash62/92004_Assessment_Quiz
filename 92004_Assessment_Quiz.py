import random


# This checks for the answers to be actual valid integers
def num_checker(question_num):
    valid = False
    while not valid:
        error = "Please enter an integer that is 1 or more"

        while True:
            to_check = input(question_num).lower()

            if to_check == "":
                return ""

            try:

                if to_check == "quit":
                    return "quit"

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


def num_questions_wanted(questions_desired):
    valid = False
    while not valid:
        error = "Please enter an integer that is 1 or more"

        while True:
            to_check = input(questions_desired).lower()

            if to_check == "":
                return ""

            try:

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
def string_checker(question_string, valid_ans):
    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        user_response = input(question_string).lower()

        for item_string in valid_ans:
            if item_string == user_response:
                return item_string

            elif user_response == item_string[0]:
                return item_string

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
To begin, choose the number of questions (or press <enter> for infinite mode).

You will receive questions about the area of different shapes, the units will be automatically accounted for; e.g you 
will not have to enter them 

You may press <enter> to skip a question but it will be marked as wrong 

Type: "quit" to exit the quiz at anytime 
 
🐥🐥🐥Good Luck🐥🐥🐥
''')
    print()
    return ""


# Main routine goes here

# what the quiz is supposed to be
end_quiz = "false"
correct_answers = 0
total_questions = 0
mode = "regular"
questions_asked = 0
feedback = ""
yes_no_list = ['yes', 'no']
quiz_history = []
all_scores = []
# Title
statement_generator("Super duper hard math test", "🤖💎")
# instructions
want_instructions = string_checker("Do you want to see the instructions?", yes_no_list)
if want_instructions == "yes":
    instructions()

# how many questions they would like to be asked of them?
num_questions = num_questions_wanted("How many questions would you like? Push <enter> for ♾️infinite mode♾️: ")

if num_questions == "":
    mode = "infinite"
    num_questions = 5

while questions_asked < num_questions:

    # creates infinite
    if mode == "infinite":
        num_questions += 1
    if end_quiz == "True":
        break
    # type of questioning based on mode
    if mode == "infinite":
        question_heading = f"\n♾️♾️♾️ Round {questions_asked + 1} (Infinite Mode) ♾️♾️♾️"
    else:
        question_heading = f"\n🎉🎉🎉 Round {questions_asked + 1} of {num_questions} 🎉🎉🎉"

    print(question_heading)

    # generates the numerical values to be used in the questions
    width = random.randint(1, 20)
    length = random.randint(1, 20)
    question_type = random.randint(1, 2)
    if length == width:
        shape = "square"
    else:
        shape = "rectangle"

    if question_type == 2:
        question_perimeter = num_checker(
            f"What is the perimeter of this {shape} if the width is {width}m and length is"
            f" {length}m? ")
        while question_perimeter == "quit" and questions_asked < 1:
            print("Cannot leave quiz on question 1")
            question_perimeter = num_checker(f"What is the area of this {shape} if the width is {width}m and length is"
                                             f" {length}m? ")

        if question_perimeter == "quit":
            end_quiz = "True"
            break
        answer = (width * 2) + (length * 2)

        if question_perimeter == "":
            print("You have skipped the question")
        else:
            print(f"You chose {question_perimeter}m")

        if question_perimeter == answer:
            result = "Congrats you are right 👌✅👍"
            print(result)
            questions_asked += 1
            correct_answers += 1
            total_questions += 1
            the_right_choice = f"2({length}) + 2({width}) which is {answer}m. You were correct ✅"
            quiz_history.append(the_right_choice)

        elif question_perimeter == "":
            result = f"2({length}) + 2({width})m. However you skipped the question ❌"
            questions_asked += 1
            total_questions += 1
            quiz_history.append(result)

        if not question_perimeter == answer and not "":
            public_result = f"❌Sorry, you are incorrect❌. If the length is {length} and the width is {width}" \
                            f" , the perimeter is " \
                            f"2({length}) + 2({width}) which is {answer}"
            print(public_result)
            result_skip = f"2({length}) + 2({width})m. However you said {question_perimeter} ❌"
            questions_asked += 1
            total_questions += 1
            quiz_history.append(result_skip)

    if question_type == 1:
        question_area = num_checker(f"What is the area of this {shape} if the width is {width}m and length is"
                                    f" {length}m? ")
        while question_area == "quit" and questions_asked < 1:
            print("Cannot leave quiz on question 1")
            question_area = num_checker(f"What is the area of this {shape} if the width is {width}m and length is"
                                        f" {length}? ")
        if question_area == "quit":
            end_quiz = "True"
            break
        answer = width * length

        if question_area == "":
            print("You have skipped the question")
        else:
            print(f"You chose {question_area}m")

        if question_area == answer:
            result = "Congrats you are right 👌✅👍"
            print(result)
            the_right_choice = f"{length} x {width} which is {answer}m^2. You were correct ✅"
            quiz_history.append(the_right_choice)
            questions_asked += 1
            correct_answers += 1
            total_questions += 1

        elif question_area == "":
            result_skip = f"{length} x {width} = {answer}m. However you skipped the question ❌"
            questions_asked += 1
            total_questions += 1
            quiz_history.append(result_skip)

        if not question_area == answer and not "":
            public_result = f"❌Sorry, you are incorrect❌. If the length is {length} and the width is {width}" \
                            f" , the area is " \
                            f"{length} x {width} which is {answer}m^2"
            print(public_result)
            result = f"{length} x {width} = {answer}m. However you said {question_area} ❌"
            questions_asked += 1
            total_questions += 1
            quiz_history.append(result)

if num_questions > 1:

    # stats of the results including the average and total as well as quiz history

    # Output stats
    print("📈📈📈 Quiz Statistics 📈📈📈")

    total = total_questions
    correct_total = correct_answers

    print(
        f"Final Score: {correct_total} out of {total}"
        f" Average: {correct_total / total:.0%}")
    print()

    see_history = string_checker("Do you want to see your quiz history? ", yes_no_list)
    if see_history == "yes":
        for item in quiz_history:
            print(item)


else:
    "..."

# final statement before quiz end

print("   Thank you for playing")
statement_generator("Super duper hard math test", "🤖💎")
print()
