# Quan, Yuan
# Dec 4, 2022

from Stack import Stack

# this function takes in a string and check if it contains valid brackets
# valid brackets include: (), <>, [], {}
# parameter: a string
# return: True if contains valid brackets, False if not

def validBrackets(input_str: str):
    # use a dictionary to map the closing brackets to the opening brackets
    brackets = {")":"(", ">":"<", "]":"[", "}":"{"}
    # use a stack to perform the checking progress
    # push opening brackets
    # if come accross a closing brackets, pop from stack to see if matches
    # return False if not match or the stack is empty
    check = Stack()
    for char in input_str:
        if char in brackets.values():
            check.push(char)
        elif char in brackets.keys():
            if check.is_empty():
                return False
            prev = check.pop()
            if prev != brackets[char]:
                return False
    # after iteration, check if stack is empty
    # return false if not empty
    # else, return True
    if not check.is_empty():
        return False
    return True


def main():
    input_str = input("input something: ")
    if validBrackets(input_str):
        print("the string is a valid set of brackets")
    else:
        print("the string is not a valid set of brackets")

if __name__ == "__main__":
    main()


