# -*- coding: cp1252 -*-
# Inlämning 4 | Uppg. 1, 2, 3
# Alexander Tallqvist

import random

# Uppg. 1

# Ask for amount of questions and difficulty of questions
amount = question_amount = input("How many questions would you like me to ask? ")
user_difficulty = input("What should the difficulty be? (number 1-10) ")

# Set dificulty to 10 if it's over 10
user_difficulty =  10 if user_difficulty > 10 else user_difficulty

# Get a max value for the random number calculation
difficulty_list = [11, 21, 31, 41, 51, 61, 71, 81, 91, 101];
difficulty = difficulty_list[user_difficulty - 1]

# Set correct answers to zero
correct = 0

# Function for checking correct answer
def check_answer(ran1, ran2, answ):
    if ran1 * ran2 == answ:
        print "Perfect!"
        return 1
    else:
        print "Sorry, the correct answer is", ran1 * ran2
        return 0


# Function for posting the end results
def end_results(questions, correct):
    percentage = round((correct/(questions/1.0)) * 100, 2)
    print "I asked you", questions, "questions, and", correct, "of theme were correct, about", percentage, "%."



while amount:
    # Generate random numbers and ask the question
    random_1 = random.randrange(1, difficulty)
    random_2 = random.randrange(1, difficulty)
    answer = input("What is " + str(random_1) + " times " + str(random_2) + "? ")

    # Check if the answer is correct
    correct += check_answer(random_1, random_2, answer)

    # Remove one from amount
    amount -= 1

    # If it's the last iteration, print the results
    if amount == 0:
        end_results(question_amount, correct)



# Uppg. 2

def man_eller_kvinna(sig):
    strang = sig.replace(" ", "")

    if len(strang) == 11:
        zzz = strang[7:10]

        if int(zzz) % 2 == 0:
            print "Du ar en kvinna."
        else:
            print "Du ar en man."
    else:
        print "Felaktigt signum"

signum = raw_input("Ange personsignum: ")
man_eller_kvinna(signum)



# Uppg. 3

# Ask for the max amount of points needed to win
max_points = input("Hur manga poang behovs att vinna? ")

# Set correct answers to zero
player_score = 0
computer_score = 0

tools = ['sten', 'sax', 'pase']
answers = [1,2,3]

# 1 = Sten
# 2 = Sax
# 3 = Påse

# Function for checking the winner of the round
# c = computer, p = player
def check_winner(c, p):
    global player_score
    global computer_score

    if c == p:
        print "Oavgjort.\n"

    elif p == 1 and c == 3 or p == 2 and c == 1 or p == 3 and c == 2:
        print get_winner_string(c, p) + " Datorn van.\n"
        computer_score += 1

    else:
        print get_winner_string(c, p) + " Du van.\n"
        player_score += 1


# Fucntion for printing the end results
def end_results():
    global player_score
    global computer_score
    print "Spelet ar slut!\n", "=" * 20
    print "Datorns poang:", computer_score
    print "Dina poang:", player_score


def get_winner_string(comp, play):
    return "Du valde " + tools[play-1] + " och datorn valde " + tools[comp-1] + "."


while True:
    # Generate random numbers and ask the question
    comp_answer = random.randrange(1, 4)
    player_answer = input("\nGor ditt val:\n1:Sten\n2:Sax\n3:Pase\n");

    # Check if the answer is correct
    if player_answer in answers:
        check_winner(comp_answer, player_answer)
    else:
        print "Felaktigt svar.\n"

    # Call end results and break if max pints is reached
    if player_score == max_points or computer_score == max_points:
        end_results()
        break
