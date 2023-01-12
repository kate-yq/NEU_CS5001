# verible = 123
# print(f"sometext {verible},{verible}")    ## outcome will be sometect 123,123
# print(verible)  ## outcome will be 123
# print(verible + verible) ## outcome will be 246

## in python, ** means power

# prints hello
def print_hello():
    print("hello")

# print_hello

# strings can be compared by alphabetical order, eg:
'car' < 'cat' # return true

# dates can be compared, in strings:
'2022/09/19'>'2002/09/19' #return true

# Fuction has 3 components: name, parameter, return
# in function comments usually use '''...'''
# can return different types in a function (if/else)
# function can access global variables, no need to input as parameters

# scripting is somthing outside functions, and if you want someone else to use 
# your code, don't write scripts
# also add a main() to call all functions, so that others can just run main()

# test in another separate file
# import original file
# call functions using filename.function()

## Scope (prioritised as follows)
# local scope
# enclosing scope
# global scope
# built-in scope

# if __name__== "__main__":
#     main()
# this is for original file to run main(), but not run main() if other files import it.


def loop_over_value(n: int):
    for i in range(n):
        print(i)
    # print from 0 to n, but not including n

# range(start[default as 0], end[need input], step[default as 1])
# will confuse if only input end and step, so need to input all 3
# range(2,10,2) will print 2,4,6,8  not including 10

# IO:
# def grades_from_file():
#     grades_file = open("fake_name.txt", 'r') #input file name, same directory
#     # 'r' means only read the file, trying to write will cause an error
#     # if want to write, can change to 'w'
#     lines = grades_file.readlines() #read line by line
#     headers = lines[0].strip().split(',')
#     names = []
#     grades = []
#     for line in lines[1:0]: 
#         values = line.strip().split(',')
#         name = values[0]
#         names.append(name)
#         student_grade = final_grade(*[int(i) for i in values[1:]]) #final_grade is a funciton previously defined
#         grades.append(student_grade)
#     for i in range(len(names)):
#         print(f"{names[i]}: {grades[i]}")
#     return grades

# good style is with open() as xxx
# for example

def write_to_file():
    with open("filename.txt", 'w') as test_file:# 'w' means overwrite(completely replace), 'a' means append
        test_file.write("HI")
        # test_file.close() # no need to call close, as the with already done it

# .csv is better to store comma separated values
# .csv will automatically recognised as spreadsheet, and can be opened by excel

# import pandas as pd
# # take care of .csv and do everything
# df = pd.read_csv("filename.csv")
# df.head() shows first 5 rows of the table (not including the title)

# import matplotlib.pyplot as plt

# def visualize_data():
#     final_grades = grades_from_file()
#     df = pd.read_csv("fake_grades.csv")
#     midterm_grades = df['midterm']
#     plt.scatter(midterm_grades, final_grades)
#     plt.show()

# import urllib.request
# can use url data

# tuple is immutable versioin of list
# use () to represednt tuple
# days_of_weeks = ("mon", "tue", "wed")
# after creation, cannot change anymore.

# pattern: x=change(x)
# if really wants to change something cannot change

# when return 2 things in a function
# it is returned as a tuple

# list = [1, 2, 3, 4]
# b = list
# b[1] = 50
# will change list as well, as they are 2 pointers point at the list
# if don't want this, b needs to be list.copy() or list[:]

# in a function, unless required, better not amend the input list
# instead, create a copy, or undo the change at the end


# from matplotlib import pyplot as plt
# # this draw a 2D chart, with points of (70,90) (90,100) (80,100)
# plt.scatter([70,90,80],[90,100,100])
# plt.show()


# import urllib.request
# import ssl

# req = urllib.request.Request("https://www.google.com")
# with urllib.request.urlopen(req) as response:
#     print(response.read())

# r = urllib.request.urlopen("https://www.google.com")
# html = str(r.read())
# for item in html.split(','):
#     if item.startswith('"headline":'):
#         print(item)


## stack-overflow means too many resurion, all of them are put into a stack
## by IDE, and run one by one
## if too many and exceed the enviroment's ability
## it will say stack-overflow

###### Recursion
# function comments:
# parameter: xxx
# return: xxx
# base case: xxx (return xx)
# recursive case: xxxxxxxxx
# (possible: recursive case 2...)

def reverse_inputs(n: int):
    if n>0:
        inp = input('input something: ')
        reverse_inputs(n-1)
        print(inp)

def unlock(passcode: str):
    if passcode == "0004":
        print("unlocked!")

def try_all():
    # call unlock with every possible 4 digit string of numbers
    try_all_helper("")

def try_all_helper(inp: str):
    if len(inp)==4:
        unlock(inp)
    else:
        for i in range(10):
            try_all_helper(inp + str(i))


## binary search by recursion
# takes in a sorted list and a number
# return true if has the uumber
def binary_search(ints: list, num: int):
    if len(ints)==0:
        return False
    elif ints[int(len(ints)/2)]<num:
        return binary_search(ints[int(len(ints)/2+1):], num)
    elif ints[int(len(ints)/2)]>num:
        return binary_search(ints[:int(len(ints)/2)], num)
    else:
        return True

# print(binary_search([1,2,3,4,5], 5))


# Recursive backtracking
# aka "exhaustive search": searchiong every possibility

# example: N Queens
# Chess played on a N*N board ()grid
# Queen can attact any piece in the same row, column, or same diagonal
# put n queens on a n*n board so that no queen is attacking each other



# raise exception
# TypeError - generally don't check the type of every parameter (don't do in hw)
# ValueError - when value is not in expected area

# def test_xx():
#     assert 6 == xx(3)
#     try:
#         xx(-10)
#     except ValueError:
#         print("specific message")
#     except TypeError:
#         print("specific message")
#     # except Exception as e:   -- genreal error, but don't do this!


# Absolute path start with "/"(starts top of your file system)
# Relative paths don't (starts where you are runnig code)

empty_set = set()
set1 = {'a', 'b', 'c'}
set2 = {'b', 'c', 'd'}
both = set1 | set2        # combine both 
intersection = set1 & set2    # return the intersection
subset1 = set1 <= set2    # 1 is a subset of 2?
subset2 = set2 <= set1    # 2 is a subset of 1?
deduction = set1 - set2   # remove elements of set2 in set1

# cannot add list to a set

# Lists, set, dictionaries, tuples .... are data structures
# if we are talking about the abstract concept a set, list ...
# then it is called an Abstract Data Type (ADT)
# ADT is generalised so that language doesn't matter


# Review: StringSet
class StringSet:
    def __init__(self):
        self.str_set = set()
    
    def add(self, item:str):
        self.check_type(item)
        self.str_set.add(item)

    def remove(self, item:str):
        self.check_type(item)
        if item not in self.str_set:
            raise RuntimeError(f"{item} is not in this StringSet")
        self.str_set.remove(item)
    
    # if not put self, need to add @staticmethod
    @staticmethod
    def check_type(item):
        if type(item) != str:
            raise TypeError("StringSet can only contain str")

    def size(self):
        return len(self.str_set)
    
    def is_empty(self):
        return self.size() == 0
    
    def __str__(self):
        return self.str_set.__str__()

# first define what the class should be able to do
# then implement it

# when we did the defining part, we define an Abstract Data Type
# ADT: is "what" (versus "how")


# ADT Stack: data structure that is ordered (like list)
# you can only add and remove from the end, check if empty
# push, pop
# Last in, first out (LIFO)
class Stack:
    def __init__(self):
        self.items = list()

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop from empty stack.")
        item = self.items[-1]
        self.items = self.items[:-1]
        return item
    
    def is_empty(self):
        return len(self.items) == 0

# ADT Queue: data structure that is ordered (like list)
# you can only add to one end, and remove from the other end, check if empty
# enqueue, dequeue
# First in, first out (FIFO)
class Queue:
    def __init__(self, items = []):
        self.items = items
    
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Cannot dequeue from empty queue")
        item = self.items[0]
        self.items = self.items[1:]
        return item

    def is_empty(self):
        return len(self.items)==0

def reverse_str(to_reverse: str):
    stack = Stack()
    for char in to_reverse:
        stack.push(char)
    to_return = ""
    while not stack.is_empty:
        to_return += stack.pop()
    return to_return

# reverse items in the queue (in place)
def reverse_queue(to_reverse: Queue):
    stack = Stack()
    while not to_reverse.is_empty:
        stack.push(to_reverse.dequeue())
    while not stack.is_empty:
        to_reverse.enqueue(stack.pop())
    return


# stable matching algorithms
# N students and N Internships
# Each student has ranked all N internships by preference
# Each internship has ranked all N students by preference

# Algorithms goal: assign students to internships such that
# there are no pairs of (student, internship) who wouls both prefer each other over their current match
# if there are no such pairs, the matching is "stable"

# Solution: 
# input:
students = [1, 2, 3, 4]
internships = [1, 2, 3, 4]
student_preferences = [
    Queue([3,2,4,1]),
    Queue([2,3,4,1]), 
    Queue([1,3,2,4]), 
    Queue([4,3,2,1])
]    # store as queues, may need to reverse the queue
internship_preferences = [
    Queue([1,2,3,4]),
    Queue([4,3,2,1]), 
    Queue([2,3,4,1]), 
    Queue([1,4,2,3])
]    # store as queues

# Gale-Shapley algorithm:
# iterate through all internships (while there are available internships)
    # each internship makes an offer to their top choice student
    # if the student is availabe
        # tentative agreement between them
    # if the student is taken
        # if student prefers this internship over the one they have
            # the student switch to this one
            # the internship they had is not available again
        # if student prefers the internship they already have
            # the internship moves to their next choice

# use a list to record the matching
# initalise all -1
# once form a match, update the corresponding match


## Sorting

# n^2 sort:
# selection sort: select the smallest from remaining and put infront
# insertion sort: pick the next to insert it into the correct place
# bubble sort: compare adjecent pairs again and again

# n log n sort:
# merge sort: recursively merge 2 sorted listed  // not in place
# quick sort?
# 2 pointer quick sort?

# Big "O" notation
# Upper bound on runtime - worst case
# F(n) = O(g(n)) means F(n) <= c*g(n) for all n greater than n_0


## Searching
# Random search (runtime: n)
# Linear search (runtime: n)
# Binary search (runtime: log n)





