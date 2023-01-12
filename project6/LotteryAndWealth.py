# Quan Yuan
# Oct 20, 2022
# this program aiming to simulate the lottery rewards and the wealth disparity between different wealth groups

import random
import numpy as np
import numpy as numpy
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib


# ----------------- THE SIMULATION ----------------- #

def generateLotteryNumbers():
    """
    Returns a list of 5 random ints between 1 and 42, inclusive, with no
    duplicates.
    """
    # YOUR CODE HERE
    # create a list to record the numbers
    # continuously generate random int when length of the list is smaller than 5
    # each time when generated a random int, check if it is already in the list
    # if not, append it into the list, else, continue to next round
    win_number = []
    while len(win_number) < 5:
        num = random.randint(1, 42)
        if num not in win_number:
            win_number.append(num)

    return win_number


def countMatches(my_list, lottery_list):
    """
    Returns the number of matches between my_list and lottery_list.
    Inputs: * my_list: A list of your lottery numbers.
            * lottery_list: A list of the winning numbers.
    """
    # YOUR CODE HERE
    match = 0
    for i in lottery_list:
        if i in my_list:
            match += 1
    return match


def playLottery():
    """
    Returns the reward after one lottery play.
    """
    # YOUR CODE HERE
    player_list = generateLotteryNumbers()
    lottery_list = generateLotteryNumbers()
    # use a list to reflect each reword, the index is the number of matches
    reward = [0, 0, 1, 11, 198, 212535]
    # deduct $1 entry cost here and return
    return reward[countMatches(player_list, lottery_list)] - 1


def getDisparityMessage(highIncomeList, lowIncomeList, decade):
    """
    Returns a string that describes the percentages of wealth possessed by the
    higher income half and lower income half for any given year.
    Inputs: *highIncomeList: The list containing wealth values for the high
            income group.
            *lowIncomeList: The list containing wealth values for low income
            group.
            *decade: The current decade as an integer.
    """
    # YOUR CODE HERE
    high_income_total = np.sum(highIncomeList)
    low_income_total = np.sum(lowIncomeList)
    # display as percentage, so multiply 100
    lowIncomePercent = round(100 * low_income_total / (low_income_total+high_income_total))
    highIncomePercent = round(100 * high_income_total / (low_income_total+high_income_total))

    message = "Decade " + str(decade) + ": The high income group possesses " +\
        str(highIncomePercent) + "% of the community's wealth, while the low"\
        "income group possesses " + str(lowIncomePercent) +\
        "% of the community's wealth."

    return message

# input parameters: a list of income of a group of people, 
#                   and the total number of people who played lottery
# output: total fund earned by lottery (revenue - total winning amount)
def simLottery(incomeList, numPlayers):
    """
    Simulates lottery play for a number of players from a given income group.
    Inputs: *incomeList: The list containing wealth values for the given
            income group.
            * numPlayers: The number of players who will play the lottery.
    """
    fund = 0
    for i in range(numPlayers):
        # YOUR CODE HERE
        # one can be drawed mulitple times
        player_index = random.randint(0, len(incomeList)-1)
        winning_amount = playLottery()
        incomeList[player_index] += winning_amount
        fund -= winning_amount
    return fund


def awardScholarship(incomeList, awardTotal):
    """
    Redistributes funds from the lottery in the form of a $1 scholarship.
    Inputs: *incomeList: The list containing wealth values for the given
            income group.
            *awardTotal: The total amount of lottery funds to be rewarded
            to members of this income group.
    """
    for i in range(awardTotal):
        # YOUR CODE HERE
        # one can be drawed multiple times
        award_index = random.randint(0, len(incomeList)-1)
        incomeList[award_index] += 1
    return


def simCommunity(years, communitySize):
    """
    Simulates the movement of money between high income and low income
    communities via the Georgia lottery and scholarship system over several
    years. Half of the community is from low income backgrounds, and half from
    high income backgrounds. The resulting wealth disparity is printed as a
    message and displayed as a scatter plot indicating overall wealth per
    person per year.
    Inputs: *years: The number of years the simulation should be run.
            *communitySize: The number of people in the community.
    """

    # ---- PART 1: Populate Wealth Lists
    # Fill highIncomeList and lowIncomeList with starting wealth values.

    highIncomeList = []
    lowIncomeList = []
    for i in range(0, communitySize, 2):
        highIncomeList.append(100)
        lowIncomeList.append(99)

    # ---- PART 2: Populate Record Lists
    # Fill highIncomeRecord and lowIncomeRecord with the starting ("year 0")
    # values from highIncomeList and lowIncomeList.

    highIncomeRecord = []
    lowIncomeRecord = []
    highIncomeRecord.append(highIncomeList.copy())
    lowIncomeRecord.append(lowIncomeList.copy())

    # simulation loop
    # if use range(years) won't reach the max, say 80,
    # therefore I changed it to range(1, years+1)
    for i in range(1, years+1):

        # ---- PART 3: Play the Lottery
        # Use the simLottery() function to simulate community
        # wealth interactions.

        fund_high = simLottery(highIncomeList, int(len(highIncomeList)*0.4))
        fund_low = simLottery(lowIncomeList, int(len(lowIncomeList)*0.6))
        
        # ---- PART 4: Award Scholarships
        # Use the awardScholarship() function to redistribute lottery funds
        # as scholarships.

        total_funds = np.maximum(fund_high+fund_low, 0)
        awardScholarship(highIncomeList, int(total_funds*0.7))
        awardScholarship(lowIncomeList, int(total_funds*0.3))

        # ---- PART 5: Update Record Lists
        # Update the income records every year.
        highIncomeRecord.append(highIncomeList.copy())
        lowIncomeRecord.append(lowIncomeList.copy())

        if i % 10 == 0:
            # ---- PART 6: Display Wealth Distribution
            # Use getDisparityMessage() to display the wealth distribution
            # every decade.
            print(getDisparityMessage(highIncomeList, lowIncomeList, i//10))
    
    # ---- PART 7: Visualize the Simulation
    # Uncomment the next line to plot the simulation.
    plotSim(highIncomeRecord, lowIncomeRecord)


# ----------------- HELPER FUNCTIONS ----------------- #
# These functions are provided for you to use.
# You do not need to change them, but feel free to explore what they do.

def plotSim(highIncomeRecord, lowIncomeRecord):
    """
    Helper function for simCommunity() to generate a scatterplot displaying
    the wealth of each person in the simulation over 8 decades. High income
    values are plotted in red. Low income values are plotted in blue.
    Inputs: *highIncomeRecord: A list of all high income wealth lists
            from each year.
            *lowIncomeRecord: A list of all low income wealth lists
            from each year.
    """
    x = np.arange(len(highIncomeRecord))

    # plot wealth records
    plotWealthRecord(x, highIncomeRecord, '#882255', '.')
    plotWealthRecord(x, lowIncomeRecord, '#44AA99', '*')

    # plot labels/legend
    plt.xlabel("Year")
    plt.ylabel("Wealth Value")
    magenta_patch = mpatches.Patch(color='#882255', label='High Income')
    teal_patch = mpatches.Patch(color='#44AA99', label='Low Income')
    plt.legend(handles=[magenta_patch, teal_patch])

    # display the plot
    plt.show()


def plotWealthRecord(x, record, markerColor, markerShape):
    """
    Helper function for plotSim(). Plots each individual wealth group.
    Inputs: *x: List of x-axis values.
            *record: The income record to be plotted.
            *markerColor: String defining the color of markers.
            *markerShape: String defining marker shape.
    """
    for i in range(len(record[0])):
        plotData = []
        for j in range(len(record)):
            plotData += [record[j][i]]
        plt.scatter(x, plotData, color=markerColor, marker=markerShape)


def simManyPlays(n):
    """
    Function to graph the total winnings of a player who plays the lottery
    n times.
    Inputs: *n: The number of times the player enters the lottery.
    """
    winnings = []
    reward = 0
    for i in range(n):
        reward += playLottery()
        winnings.append(reward)
    plt.xlabel("Number of Lottery Plays")
    plt.ylabel("Winnings")
    plt.plot(winnings)
    plt.legend()
    plt.show()

# ----------------- MAIN FUNCTION ----------------- #


def main():
    # Simulate 1000 plays by one person and plot the winnings.
    simManyPlays(1000)

    # Simulate a community playing Lottery 5 with 30 people for 80 years.
    simCommunity(80, 30)

if __name__ == "__main__":
    main()
