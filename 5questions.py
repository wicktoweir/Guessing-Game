from random import randint

print "Welcome to Animal Guess! Here we will give you clues and you will try to tell us what animal we are thinking."
print "Five clues, five guesses, give it a shot!"

first_question = ["First clue: Some would guess my hearing is better than most\t",
                  "I walk in a different way than most\t",
                  "I eat things that make me a good role model for humans\t",
                  "There are songs about the way I move\t",
                  "A certain holiday would lead one to believe I do a lot with eggs.\t"]

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


def ask_question(question_num, correct_answer):
    count = 0
    answer = raw_input(question_num[count]).lower()
    hint_num = 1
    while count <= 4 and hint_num <=5:
        hint_num += 1
        count += 1
        if answer == correct_answer:
            print random_responses[randint(0,len(random_responses)-1)]
            break
        else:
            print random_retries[randint(0,len(random_retries)-1)]

        answer = raw_input(question_num[count]).lower()
    else:
        print "It was a %s! Thanks for Playing" % correct_answer


ask_question(first_question, "rabbit")

print "Alright, let's try another"

ask_question(second_question, "donkey")



    

