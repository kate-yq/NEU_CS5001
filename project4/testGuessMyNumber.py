# Quan Yuan, Oct 5, 2022

# testing the indivial functions in guessMyNumber

import guessMyNumber

def main():
    test_high_low_good()
    test_high_low_bad()
    test_high_low_turn_efficiency_good()
    test_high_low_turn_efficiency_bad()

    test_hot_cold_good()
    test_hot_cold_bad()
    test_hot_cold_turn_efficiency_good()
    test_hot_cold_turn_efficiency_bad()

def test_high_low_good():
    assert guessMyNumber.high_low(5, 5) == 0

def test_high_low_bad():
    '''guessing -1 which is out of said range'''
    assert guessMyNumber.high_low(10, -1) == -1

def test_high_low_turn_efficiency_good():
    assert guessMyNumber.high_low_turn_efficiency(12, 1024) == False

def test_high_low_turn_efficiency_bad():
    '''when there is only 0 and 1 to guess, the worst case will take 2 attempts, instead of 1'''
    assert guessMyNumber.high_low_turn_efficiency(2, 1)==True

def test_hot_cold_good():
    assert guessMyNumber.hot_cold(10, 5, 15) == 2

def test_hot_cold_bad():
    '''we are guessing -1 which is out of said range, but hotter than last time'''
    assert guessMyNumber.hot_cold(4, -1, 11) == 1

def test_hot_cold_turn_efficiency_good():
    assert guessMyNumber.hot_cold_turn_efficiency(21, 1024) == False

def test_hot_cold_turn_efficiency_bad():
    '''when there is only 0 and 1 to guess, the worst case will take 2 attempts, instead of 1'''
    assert guessMyNumber.hot_cold_turn_efficiency(2, 1) == True


if __name__ == "__main__":
    main()