from random import randint

print "Welcome to Animal Guess! Here we will give you clues and you will try to tell us what animal we are thinking."
print "Five clues, five guesses, give it a shot!"

def load_question():
    with open("questions/Rabbit") as f:
        content = f.readlines()
    return content

second_question = ["First clue: I eat\t",
                  "I drink\t",
                  "I love\t",
                  "I fart\t",
                  "I poo.\t"]

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
    count = 1
    answer = raw_input(question[count]).lower()
    while count <= 4:
        if answer == correct_answer:
            print random_responses[randint(0,len(random_responses)-1)]
            break
        else:
            if count == 4:
                print random_retries[randint(0,len(random_retries)-1)] + " Last clue..."
            else:
                print random_retries[randint(0,len(random_retries)-1)] + " Clue " + str(count +1) + "..."


        answer = raw_input(question[count]).lower()
        count += 1
    else:
        print "It was a %s! Thanks for Playing" % correct_answer


ask_question(load_question(), "rabbit")

print "Alright, let's try another"

ask_question(second_question, "donkey")



    

