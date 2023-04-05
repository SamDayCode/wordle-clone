import random
from random import randint

import wordle_functions
from wordle_functions import comparewords

target_word_file = open("word-bank/target_words.txt", "r")
target_word_list = list()
for line in target_word_file:
    line = line.split()
    for word in line:
        target_word_list.append(word)

all_word_file = open("word-bank/all_words.txt", "r")
all_word_list = list()
for line in all_word_file:
    line = line.split()
    for word in line:
        all_word_list.append(word)

#print(target_word_list)
random_integer = randint(0,len(target_word_list)) #measures the amount of items in the list to be used as a random word picker
print(random_integer)
print(target_word_list[random_integer])
target_word = target_word_list[random_integer]

attempt_counter = int(6) #6 attempts to guess the correct word

def comparewords(correct_word, guess_word):
    guess_word_letter1 = "-"
    guess_word_letter2 = "-"
    guess_word_letter3 = "-"
    guess_word_letter4 = "-"
    guess_word_letter5 = "-"

    if guess_word[0] in correct_word:
        guess_word_letter1 = "O"
    if guess_word[0] == correct_word[0]:
        guess_word_letter1 = "X"

    if guess_word[1] in correct_word:
        guess_word_letter2 = "O"
    if guess_word[1] == correct_word[1]:
        guess_word_letter2 = "X"

    if guess_word[2] in correct_word:
        guess_word_letter3 = "O"
    if guess_word[2] == correct_word[2]:
        guess_word_letter3 = "X"

    if guess_word[3] in correct_word:
        guess_word_letter4 = "O"
    if guess_word[3] == correct_word[3]:
        guess_word_letter4 = "X"

    if guess_word[4] in correct_word:
        guess_word_letter5 = "O"
    if guess_word[4] == correct_word[4]:
        guess_word_letter5 = "X"

    score_answer = guess_word_letter1,guess_word_letter2,guess_word_letter3,guess_word_letter4,guess_word_letter5
    return score_answer


##Gamestart##
print("A random 6-Letter word has now been chosen. You have", attempt_counter, " attempts remaining (Real words only!). \n Goodluck!")

while attempt_counter > 0:
    player_guess = input("Your Guess:")
    if player_guess.lower() in all_word_list:
        score = comparewords(target_word, player_guess.lower())
        print(score)
        attempt_counter = attempt_counter - 1

    else:
        print("Invalid Guess - Try again")
        continue
