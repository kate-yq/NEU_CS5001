#Template by Lindsay Jamieson
# Quan, Yuan
# Oct 31, 2022


# parameter: the amount of level for the desired triangle
# return: a list of lists, with each list representing a line of the Hosoya's triangle
def computeTriangle(levels):
    ''' This function is recursive.  It will compute the levels of Hosoya's triangle.
    It does NOT print Hosoya's triangle.  Remember that each location in the
    triangle is the sum of the two diagonally above it with the top two rows being:
    1
    1 1
    Input: The number of rows to generate
    Output: The triangle as a list of lists.'''
    # base case: level 1 is [1], level 2 is [1, 1]
    # corner case: level <= 0, return an empty list
    # recursive case: based on previous triangle, generate the last line, and append it to previous triangle
    if levels <= 0:     # corner case
        return []
    elif levels == 1:    # base case 1
        return [[1]]
    elif levels == 2:    # base case 2
        return [[1], [1,1]]
    else:
        # recursive case:
        # based on the n-1 level triangle, get the last 2 lines
        # then compute the current line based on the previous 2 lines
        prev_triangle = computeTriangle(levels-1)
        above_1_line = prev_triangle[-1]
        above_2_line = prev_triangle[-2]
        cur_line = []
        # the first n-2 elements are equal to sum of same-index in previous 2 lines
        for i in range(levels-2):
            cur_line.append(above_1_line[i]+above_2_line[i])
        # the n-1 element is equal to the last element in previous line
        cur_line.append(above_1_line[-1])
        # the n element is equal to the first element
        cur_line.append(cur_line[0])

        prev_triangle.append(cur_line)
        return prev_triangle


# parameter: the list of lists representing a Hosoya's triangle, and the total levels
# print the triangle
def printTriangle(triangle, levels):
    ''' This function will print a left justified copy of Hosoya's triangle.
    Input: triangle - the values to be printed, levels - the height of the triangle
    Output: NONE'''
    # corner case: levels <= 0, print empty list
    if levels <= 0:
        print()
        return

    for i in range(levels):
        for element in triangle[i]:
            print(element, end=" ")
        print()


def main():
    '''This is the main control function for the program.
    You should ask the user how many levels and then compute the triangle
    recursively. Then you should print the triangle.'''
    levels = int(input("How many levels? "))
    triangle = computeTriangle(levels)
    printTriangle(triangle, levels)

if __name__=="__main__":
    main()