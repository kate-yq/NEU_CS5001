# Quan, Yuan
# this projrct is to realize the spaceman game
# it picks a random word from a list, and tell the user how many characters are there. Then let the user guess
# once the user guess right, it will reveal the corresponding letter(s)
# it tell the user lose when the user make 6 wrong guesses

import random

WRONG_ATTEMPT = 6

# create a list of 20 words between 5 and 15 characters
DICT = ["accessability", "acknowledgement", "biotechnology", "classification", "confidentiality",
            "dehydrogrnate", "environmental", "gynechologist", "heterosexual", "immunology",
            "kingdergarden", "mathmetician", "neuroscientist", "overreacted", "proprietorship",
            "quantitative", "restrictiveness", "sarcasm", "thermotherapy", "vulnerable"]



# take the list of word as input
# then pick a random word and return that word (as list for easier operation)
def random_word(dict):
    i = random.randint(0, len(dict)-1)
    return dict[i]


# take the target word as input, record the wrong attempts the client made
# if wrong attempts reached WRONG_ATTEMPT, tell the client lose the game
# if the client get all characters, tell the client win the game
def spaceman(word):
    temp = list("_"*len(word))
    print(f"now let's play spaceman game! My word is: {toString(temp)}")

    wrong_attempt = 0

    # keep asking client to guess letters until
    # either the client guess all characters or guess wrong 6 times
    while (wrong_attempt < WRONG_ATTEMPT) & ("_" in temp):
        letter = input("guess a letter: ")

        # check if the guessed letter is in the word, AND not previously guessed letters
        # if both, update the corresponding letters in temp and print
        # if not, increase wrong attemp by 1, and print the corresponding problem
        if letter not in word:
            wrong_attempt +=1
            print("the letter does not exist.")
        elif letter in temp:
            wrong_attempt +=1
            print("you have already guessed the letter.")
        else: 
            for i in range(len(word)):
                if word[i] == letter:
                    temp[i] = letter
            print(f"the letter exists! now the word is {toString(temp)}")
    
    # check why the while-loop breaks, if it's because 6 wrong guess, tell the lose information
    # if it's because all characters are revealed, tell the win information
    if wrong_attempt == WRONG_ATTEMPT:
        print(f"Sorry, you have reached {WRONG_ATTEMPT} wrong attemps. You've LOST!")
    else:
        print("You WIN!")


# input a list and return all elements joint as a single string
def toString(list):
    str = ""
    for i in range(len(list)):
        str += list[i]
    return str


def main():
    word = random_word(DICT)
    spaceman(word)


if __name__ == "__main__":
    main()
