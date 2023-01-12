# question 1
# parameter: amount of number asking from user
# prints the min, max, and average of those numbers.
# this problem should be done without using a list
# do not need to handle the case where a user enters something other than a number
def print_min_max_average(length: int):
    if length == 0:
        print(f"{length} numbers needed")
        return
    elif length < 0:
        print(f"Illegal input as the required amount is {length}")
        return
    elif length == 1:
        print(f"Please enter {length} numbers.")
    else: 
        print(f"Please enter {length} numbers.")

    # ask for first input
    num = int(input("Please enter a number: "))
    # use 3 pointers to record the current min, max and sum
    min = num
    max = num
    sum = num

    # for resting numbers, use for loop to ask for input
    for i in range(1,length):
        num = int(input("Please enter a number: "))
        sum += num
        if num < min:
            min = num
        elif num > max:
            max = num
    avg = sum / length
    print(f"Minimum: {min}")
    print(f"Maximum: {max}")
    print(f"Average: {avg}")


# question 2
# takes a string (start) and a list of strings (opt) as a parameter
# returns True if any of the strings in opt starts with the string start
# else return False
# Do not make any changes to the list passed as a parameter
# can use the built-in Python startswith() function
# case sensitive
def any_starts_with(start: str, opt: list):
    for s in opt:
        if s.startswith(start):
            return True
    return False

# question 3
# reads in 2 files in the same directory, each contains a list of vector
# parameters are the names of 2 files
# return dot product of these vectors
# (A dot product is defined as the sum of the elementwise product of the two vectors.
#  For example, the dot product of two vectors [a, b, c] and [d, e, f] is ad + be + cf.)
def dot_product(file1: str, file2: str):
    # open file1 and reads in line by line
    file_1 = open(file1, 'r')
    vectors_1 = file_1.readlines()
    # open file2 and reads in line by line
    file_2 = open(file2, 'r')
    vectors_2 = file_2.readlines()

    # vectors_1 and vectors_2 are 2 list of string, shares same length
    # and each element ends with "\n"
    # use a for loop to directly compute the dot product
    product = 0
    for i in range(len(vectors_1)):
        x = float(vectors_1[i].strip())
        y = float(vectors_2[i].strip())
        product += (x*y)
    return product



def main():
    # print_min_max_average(-2)
    print(any_starts_with("cat", []))
    # print(dot_product("test_x.txt", "test_y.txt"))

main()



