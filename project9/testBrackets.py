# Quan, Yuan
# Dec 4, 2022

import Brackets

def test_validBrackets():
    case1 = "cgnv [sgvth]hyt{rh[ad]htr}fdsg<(hi[{hi}])>"    # valid
    case2 = "[[[]{gbnrj},udsdc](),<>"    # extra opening
    case3 = "as{x}dves[s(gh)<dfh>)r]rth(hbfgb)r"    # extra closing
    case4 = "<(>)"    # not matching
    case5 = ""    # valid
    assert Brackets.validBrackets(case1) == True
    assert Brackets.validBrackets(case2) == False
    assert Brackets.validBrackets(case3) == False
    assert Brackets.validBrackets(case4) == False
    assert Brackets.validBrackets(case5) == True

def main():
    test_validBrackets()
    print("all test passed!")

if __name__ == "__main__":
    main()
