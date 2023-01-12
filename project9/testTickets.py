# Quan, Yuan
# Dec 4, 2022

from Queue import Queue
import Tickets

def test_new_joiner():
    line = Queue()
    amount = 0
    new_amount = Tickets.new_joiner(line, amount)
    assert new_amount >= amount
    assert new_amount <= amount+2

def test_serve():
    line = Queue([0,1,2,3,4])
    amount = 0
    new_amount = Tickets.serve(line, amount)
    assert new_amount == amount+1
    assert line.size() == 4


def main():
    test_new_joiner()
    test_serve()
    print("all tests passed!")


if __name__=="__main__":
    main()
