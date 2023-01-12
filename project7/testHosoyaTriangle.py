# Quan, Yuan
# Oct 31, 2022

import Lab7HosoyaTriangle

def test_computeTriangle():
    expect = [[1],[1,1],[2,1,2],[3,2,2,3],[5,3,4,3,5]]
    assert Lab7HosoyaTriangle.computeTriangle(5) == expect
    assert Lab7HosoyaTriangle.computeTriangle(0) == []
    assert Lab7HosoyaTriangle.computeTriangle(-5) == []
    assert Lab7HosoyaTriangle.computeTriangle(2) == [[1], [1,1]]

def main():
    test_computeTriangle
    print("all test passed!")

if __name__=="__main__":
    main()
