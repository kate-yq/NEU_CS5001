import dec1lab

def test_student_prefers_i_over_current():
    student_ranking = dec1lab.Queue([1,2,3,4,5])
    assert dec1lab.student_prefers_i_over_current(student_ranking, 5)==True
    assert dec1lab.student_prefers_i_over_current(student_ranking, 3)==True
    assert dec1lab.student_prefers_i_over_current(student_ranking, 1)==True
    assert dec1lab.student_prefers_i_over_current(student_ranking, 3)==False

def test_find_matches():
    student_preferences = [
        dec1lab.Queue([0,1]),
        dec1lab.Queue([1,0])
    ]
    internship_preferences = [
        dec1lab.Queue([2,3]),
        dec1lab.Queue([3,2])
    ]
    expect = [(2,0), (3,1)]
    assert dec1lab.find_matches(student_preferences, internship_preferences) == expect

def main():
    test_student_prefers_i_over_current()
    test_find_matches()
    print("all test passed!")

if __name__ == "__main__":
    main()
