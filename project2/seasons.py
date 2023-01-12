# Quan Yuan, Sep 20,2022, CS5001
# Project 2 code file No.3
# this program takes in a date and return the season of it

# the string comparison will stop when there is a difference in the digits
# so if enter date in the sequence of mm/dd/yyyy, the year won't affect the results
def season(date):
    if date<"03/20":
        print("winter")
    elif date<"06/21":
        print("spring")
    elif date<"09/22":
        print("summer")
    elif date<"12/21":
        print("fall")
    else:
        print("winter")

date = input('please input a date(mm/dd/yyyy): ')

season(date)
