# 4 tests for each function
# 1 general case, 1 edge case, 1 malicious case
import sep29lab

def main():
    # the followings are testing the federal tax function in sep29la.py
    test_fedtax_general()
    test_fedtax_edge_1()
    test_fedtax_edge_2()
    test_fedtax_malicious()
    # the followings are testing the grade calculator function in sep29lab.py
    test_grade_general()
    test_grade_edge()
    test_grade_malicious_1()
    test_grade_malicious_2()


def test_fedtax_general():
    assert 18021 == sep29lab.federaltax(100000)

def test_fedtax_edge_1():
    assert 0 == sep29lab.federaltax(0)

def test_fedtax_edge_2():
    assert 334072.25 == sep29lab.federaltax(1000000)

def test_fedtax_malicious():
    assert -1 == sep29lab.federaltax(-100)

def test_grade_general():
    assert 88 == sep29lab.gradeCalculator(90,90,100,90,80,80)

def test_grade_edge():
    assert 0 == sep29lab.gradeCalculator(0,0,0,0,0,0)

def test_grade_malicious_1():
    assert -1 == sep29lab.gradeCalculator(-20,100,100,100,100,100)

def test_grade_malicious_2():
    assert -1 == sep29lab.gradeCalculator(10000,0,100,0,0,0)

# if __name__=="__main__":
#     main()


main()