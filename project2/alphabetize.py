# Quan Yuan, Sep 20,2022, CS5001
# Project 2 code file No.2
# this program takes in 5 words and return all of them alphabetically

# take inputs
a = input("please input the first word: ")
b = input("please input the second word: ")
c = input("please input the third word: ")
d = input("please input the fourth word: ")
e = input("please input the fifth word: ")

# screening the words, and switch the new screened element to the proper position
# of the organised array
if b<a:
    a,b = b,a
if c<b:
    b,c = c,b
    if b<a:
        a,b = b,a
if d<c:
    c,d = d,c
    if c<b:
        b,c = c,b
        if b<a:
            a,b = b,a
if e<d:
    d,e = e,d
    if d<c:
        c,d = d,c
        if c<b:
            b,c = c,b
            if b<a:
                a,b = b,a
print(a,b,c,d,e)
