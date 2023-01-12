# Quan Yuan, Sep 20,2022, CS5001
# Project 2 code file No.1
# this program takes in 3 numbers and return the largest, smallest and averge.

def find_3_numbers(a, b, c):
    max = a
    min = a
    # calculate the average
    avg = (a+b+c)/3
    # find max and min
    if (b > max):
        max = b
    elif (b < min):
        min = b
    if (c > max):
        max = c
    elif (c < min):
        min = c
    print(
        f"the largest number is {max}, the smallest number is {min}, and the average is {avg}")

# take inputs
a = int(input("please input your first number: "))
b = int(input("please input your second number: "))
c = int(input("please input your third number: "))

find_3_numbers(a, b, c)
