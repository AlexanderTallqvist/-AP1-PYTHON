# -*- coding: cp1252 -*-
# Tutorial övning
# Alexander Tallqvist


import random

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
