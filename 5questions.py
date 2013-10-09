import random
import os
from random import randint

print "Welcome to Animal Guess! Here we will give you clues and you will try to tell us what type of animal we are thinking. No specifics, just generic animal name such as goat."
print "Five clues, five guesses, give it a shot!"

def load_question(question):
    with open("questions/%s" % question) as f:
        content = f.readlines()
    return content



random_responses = ["You got it!",
                    "Good job, that's it!",
                    "Alright, that's correct!",
                    "Excellent, you guessed it!",
                    "Great work, you got it!"]

random_retries = ["Not quite.",
                  "Try again.",
                  "Give it another shot.",
                  "Don't give up. Keep guessing."]


def ask_question(question, correct_answer):
    count = 0
    while count <= 4:
        answer = raw_input(question[count]).lower()
        if answer == correct_answer:
            print random_responses[randint(0,len(random_responses)-1)]
            break
        else:
            if count == 3:
                print random_retries[randint(0,len(random_retries)-1)] + " Last clue..."
            else:
                print random_retries[randint(0,len(random_retries)-1)] + " Clue " + str(count + 2) + "..."

        count += 1
    else:
        print "It was a %s! Thanks for Playing" % correct_answer
more_questions = True
while more_questions:
    question_answer = random.choice(os.listdir("questions"))
    ask_question(load_question(question_answer), question_answer.lower())
    if raw_input("Would you like another question? y/n ").lower() != "y":
        more_questions = False
        print "Thanks for playing!"







    

