# testing of distance(a, b) function in oct6-2.py

import lab.oct6lab

def test_levenshtein_distance_1():
    assert lab.oct6lab.levenshtein_distance("mango", "mango") == 0

def test_levenshtein_distance_2():
    assert lab.oct6lab.levenshtein_distance("apple", "mango") == 5

def test_levenshtein_distance_3():
    assert lab.oct6lab.levenshtein_distance("aa", "mango") == 5

def main():
    test_levenshtein_distance_1()
    test_levenshtein_distance_2()
    test_levenshtein_distance_3()

if __name__ == "__main__":
    main()