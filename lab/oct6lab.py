# this program random draw a 5-letter words, and ask the client to guess
# CHANGES EXPLANATION: the original file name is oct6-2.py, which will cause some error when import to others
# so the name is changed to oct6.py


# if needed: pip install python-Levenshtein
from Levenshtein import distance
import random


# this function takes in 2 words
# and return the number of different characters in between
# CHANGES EXPLANATION: re-indent the function body with tab/4 spaces, instead of 2 spaces
def levenshtein_distance(word1, word2):
    return distance(word1, word2)

###### as the fuction just return distance(), so it is unnassary. Just call distance ()

# this function take the target word as parameter
# ask for an input guess and determine whether the guess is correct
# CHANGES EXPLANATION: delete if...else... statement, and delete the break command
#   re-write the code to make it easier to understand
#   re-name the function so the name can relect what this is for
def ask_client_to_guess(random_word):
    guess = input('Your guess: ')

    while guess != random_word:
        print(f"Only {levenshtein_distance(guess, random_word)} characters off")
        guess = input('Your guess: ')

    print("Great job!")


# the main() will get all 5-letter words from dictionary, and append them into a list
# then random draw a word from the list, and ask client to guess
# CHANGES EXPLANATION: re-write the code, as some of them are duplicate with ask_client_to_guess function
#   delete the duplicate part and let the ask_client_to_guess functiont to do all the work
def main():
    dictionary = get_dictionary()
    five_letter_words = []
    for i in range(0,len(dictionary)):
        if len(dictionary[i]) == 5:
            five_letter_words.append(dictionary[i])
    
    # draw a random word from the list
    random_index = random.randint(0,len(five_letter_words))
    random_word = five_letter_words[random_index]
    
    ask_client_to_guess(random_word)

###### main() should be more simple. So create another function to create list, pick random word


# Don't worry about this function for now
def get_dictionary():
    return [word.strip() for word in open('dictionary.txt', 'r').readlines()]



# CHANGES EXPLANATION: add a if condition so than the main() function will only run when this file is executed
#   instead of when others import this file, the main() function will also run
if __name__ == "__main__":
    main()