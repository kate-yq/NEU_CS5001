# Quan Yuan, Sep29 2022
# generate a random card and ask the user to guess the color
import sys
import random

def main():
    # the program picks a card
    value = getValue()
    suit = getSuit()

    if len(sys.argv)>1:
        # if the user input/guessed a color
        # tell the user if it is correct
        color = sys.argv[1]
        if (suit=="Diamonds") or (suit=="Hearts"):
            if (color=="Red") or (color=="red"):
                print("You guess correct! My card is: ")
                printCard(value, suit)
            elif (color=="Black") or (color=="black"): 
                print("You guess wrong! My card is: ")
                printCard(value, suit)
            else:
                # if user make malicious input
                # notify and tell the result
                print("plese guess only red or black next time. My card is: ")
                printCard(value, suit)
        else:
            if (color=="Black") or (color=="black"):
                print("You guess correct! My card is: ")
                printCard(value, suit)
            elif (color=="Red") or (color=="red"): 
                print("You guess wrong! My card is: ")
                printCard(value, suit)
            else:
                # if user make malicious input
                print("plese guess only red or black next time. My card is: ")
                printCard(value, suit)
    else:
        # if the user didn't input/guess a color
        # tell the user the result
        print('you did not guess the card! My card is: ')
        printCard(value, suit)

# generate a random suit
def getSuit():
    list = ['Diamonds', 'Hearts', 'Clubs', 'Spades']
    return random.choice(list)

# generate a random value
def getValue():
    list = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    return random.choice(list)

# print the card in certain form
def printCard(value, suit):
    print(f'{value} of {suit}')

if __name__=="__main__":
    main()

