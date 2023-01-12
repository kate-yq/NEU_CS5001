# Quan Yuan, Oct 5, 2022

# this file contains a main() function that reads in a number from command line as the maximum value
# and 3 functions that randomly draw a number from the range, then help the user to guess the number

import sys
import random
import math


# main() function: reads in a number from command line as maximum value of the guessing range
# default range is 100
# draw a random number from input range (0 to maximum value), and ask client to guess
# until guess correct, check total attemps and determine whether it is effective

def main():
    max = 100

    if len(sys.argv) == 1:
        # when the client did not input anything in command line
        # use default range as 0-100
        print("you didn't input a number, so I will choose from 0(inclusive) to 100 (inclusive)")
    elif int(sys.argv[1]) > 0:
        # when input number>0, use this as maximun value if the range (inclusive)
        max = int(sys.argv[1])
    else:
        # when input number<=0, use default range
        print("your input number is illegal, so I will choose from 0(inclusive) to 100 (inclusive)")

    # first run
    print("First run: now you can guess my number, and I will tell you it is higher or lower.")
    guess_high_low(max)

    # second run
    print("Second run: now you can guess my number, and I will tell you it is hotter or colder.")
    guess_hot_cold(max)


# input max as max value
# random draw a number from 0 to max(inclusive), and ask client to guess
# tell whether it is higher or lower, and decide whether the turns are efficient

def guess_high_low(max):
    '''draw a number from 0 to max, both sides are inclusive'''
    num = random.randint(0, max)
    guess = int(input('Make a guess: '))
    '''record the turns of guess'''
    turns = 1

    while high_low(num, guess) != 0:
        guess = int(input('Make a guess: '))
        turns += 1

    high_low_turn_efficiency(turns, max)


# input max as max value
# random draw a number from 0 to max(inclusive), and ask client to guess
# tell whether it is getting hotter or colder, and decide whether the turns are efficient

def guess_hot_cold(max):
    '''draw a number from 0 to max, both sides are inclusive'''
    num = random.randint(0, max)
    '''take in first guess and record the attempt'''
    last_guess = int(input('Make a guess: '))
    turns = 1

    '''if luckily guess right, no need to guess second time'''
    if last_guess == num:
        print(f"Correct! Mumber is {num}.")
    else:
        guess = int(input('Make a second guess: '))
        turns += 1
        while hot_cold(num, guess, last_guess) != 0:
            last_guess = guess
            guess = int(input('Make a guess: '))
            turns += 1

    hot_cold_turn_efficiency(turns, max)


# tell the client whether the guess is higher than the number or lower than the number
# return -1 if lower, 1 if higher and 0 if correct

def high_low(num, guess):
    if guess > num:
        print("Your guess is higher than my number")
        return 1
    elif guess < num:
        print("Your guess is lower than my number")
        return -1
    else:
        print(f"Correct! Mumber is {num}.")
        return 0


# tell the client whether the guess is hotter or colder than last guess
# return -1 if getting colder, 1 if getting hotter, 2 if neither, 0 if correct

def hot_cold(num, guess, last_guess):
    if guess == num:
        print(f"Correct! Mumber is {num}.")
        return 0
    elif abs(guess-num) > abs(last_guess-num):
        print("Getting colder")
        return -1
    elif abs(guess-num) < abs(last_guess-num):
        print("Getting hotter")
        return 1
    else:
        '''the 2 guess have equal length'''
        print("Neither hotter nor colder")
        return 2


# take the input as turns of guesses and range, then determine whether it is efficient
# the most efficient algorithm is using binary search
# and the turns of guess in binary search is log2(total numbers) rounding up to the closest int
# return True if effective and False if ineffective

def high_low_turn_efficiency(turns, max):
    efficent = math.log(max+1, 2)//1 + 1
        
    if turns > efficent:
        print(f"you guessed {turns} turns, which is not the most efficient way")
        return False
    else:
        print(f"you guessed {turns} turns, which is very efficient")
        return True


# take the input as turns of guesses and range, then determine whether it is efficient
# an almost most efficient algorith is using binary search
# and the turns of guess in binary search is 2*log2(total numbers) rounding up to the closest int
# return True if effective and False if ineffective

def hot_cold_turn_efficiency(turns, max):
    efficent = 2 * (math.log(max+1, 2)//1)
    
    if turns > efficent:
        print(f"you guessed {turns} turns, which is not the most efficient way")
        return False
    else:
        print(f"you guessed {turns} turns, which is very efficient")
        return True


if __name__ == "__main__":
    main()
