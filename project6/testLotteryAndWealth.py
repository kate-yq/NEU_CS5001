import LotteryAndWealth

# test if generateLotteryNumbers can generate a list of 5 int, and contains no duplicates
def testGenerateLotteryNumbers():
    nums = LotteryAndWealth.generateLotteryNumbers()
    nums.sort()
    duplicate = False
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            duplicate = True
    assert duplicate==False and len(nums)==5

# test if countMatches() can return the correct answer:
def testCountMatches():
    list_1 = [9, 2, 40, 32, 5]
    list_2 = [2, 5, 10, 3, 16] 
    assert LotteryAndWealth.countMatches(list_1, list_2)==2

# test if playLottery() will generate a reward in $0, 1, 11, 198, 212535
def testPlayLottery():
    rewards = [-1, -1, 0, 10, 197, 212534]
    win = LotteryAndWealth.playLottery()
    assert win in rewards

# test if getDisparityMessage() returns the correct message
def testGetDisparityMessage():
    high_income = [100, 100]
    low_income = [50, 30, 50, 30, 20, 20]
    message = "Decade 1: The high income group possesses 50% of the community's wealth, while the lowincome group possesses 50% of the community's wealth."
    assert LotteryAndWealth.getDisparityMessage(high_income, low_income, 1)==message

# test if sim lottery will amend the input list accorrdingly
def testSimLottery():
    income_list = [10, 10, 10, 10, 10]
    income_list_copy = income_list.copy()
    fund = LotteryAndWealth.simLottery(income_list, 10)
    changed = False
    # a very minimal chance that all 10 lottery play get 0 award
    for i in range(len(income_list)):
        if income_list[i] != income_list_copy[i]:
            changed = True
    assert changed==True
    assert fund<=10

# test if awardScholarship will amend the input list accorrdingly
def testAwardScholarship():
    income_list = [10, 10, 10, 10, 10]
    income_list_copy = income_list.copy()
    LotteryAndWealth.awardScholarship(income_list, 5)
    changed = False
    for i in range(len(income_list)):
        if income_list[i] > income_list_copy[i]:
            changed = True
    assert changed==True


def main():
    testGenerateLotteryNumbers()
    testCountMatches()
    testPlayLottery()
    testGetDisparityMessage()
    testSimLottery()
    testAwardScholarship()
    print("All test passes!")

if __name__=="__main__":
    main()