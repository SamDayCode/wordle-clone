guess_word = 'hello'
guess_user_word = 'allow'

def compare(word, user_word):
    word_letter1 = word[0]
    word_letter2 = word[1]
    word_letter3 = word[2]
    word_letter4 = word[3]
    word_letter5 = word[4]
    #x = print(word_letter1, word_letter2, word_letter3, word_letter4, word_letter5)

    user_word_letter1 = user_word[0]
    user_word_letter2 = user_word[1]
    user_word_letter3 = user_word[2]
    user_word_letter4 = user_word[3]
    user_word_letter5 = user_word[4]
    #y = print(user_word_letter1, user_word_letter2, user_word_letter3, user_word_letter4, user_word_letter5)
    return x, y

compare(guess_word, guess_user_word)