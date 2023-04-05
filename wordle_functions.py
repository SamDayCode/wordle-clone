def comparewords1(word, user_word):
    word_letter1 = word[0]
    word_letter2 = word[1]
    word_letter3 = word[2]
    word_letter4 = word[3]
    word_letter5 = word[4]
    x = print(word_letter1, word_letter2, word_letter3, word_letter4, word_letter5)

    user_word_letter1 = user_word[0]
    user_word_letter2 = user_word[1]
    user_word_letter3 = user_word[2]
    user_word_letter4 = user_word[3]
    user_word_letter5 = user_word[4]
    y = print(user_word_letter1, user_word_letter2, user_word_letter3, user_word_letter4, user_word_letter5)
    return x, y

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