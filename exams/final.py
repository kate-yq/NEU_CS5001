import unittest

class IntQueue():
    def __init__(self):
        self.items = list()

    # add the input parameter to the end of the list
    def enqueue(self, item):
        if type(item) != int:
            raise TypeError("have to enqueue an int")
        else:
            self.items.append(item)

    # return and remove the fisrt element in the list
    def dequeue(self):
        if len(self.items)==0:
            raise IndexError("cannot dequeue from an empty Queue")
        else:
            item = self.items[0]
            self.items = self.items[1:]
        return item

    # return True if queue is empty, return False otherwise
    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return str(self.items)



class TestIntQueue(unittest.TestCase):
    def test_enqueue_general(self):
        iq = IntQueue()
        iq.enqueue(1)
        iq.enqueue(2)
        expected = "[1, 2]"
        self.assertEqual(str(iq), expected)

    def test_enqueue_edge(self):
        iq = IntQueue()
        self.assertEqual(str(iq), "[]")

    def test_enqueue_invalid(self):
        iq = IntQueue()
        try:
            iq.enqueue("1")
        except TypeError as e:
            print("catched an expected error:")
            print(e)

    def test_dequeue_general(self):
        iq = IntQueue()
        iq.enqueue(1)
        iq.enqueue(2)
        iq.dequeue()
        expected = "[2]"
        self.assertEqual(str(iq), expected)

    def test_dequeue_edge(self):
        iq = IntQueue()
        iq.enqueue(1)
        iq.dequeue()
        self.assertEqual(str(iq), "[]")

    def test_dequeue_invalid(self):
        iq = IntQueue()
        try:
            iq.dequeue()
        except IndexError as e:
            print("catched an expected error:")
            print(e)

    def test_is_empty(self):
        iq = IntQueue()
        self.assertTrue(iq.is_empty())
        iq.enqueue(1)
        self.assertFalse(iq.is_empty())
    
    def test_str(self):
        iq = IntQueue()
        self.assertEqual(str(iq), "[]")
        iq.enqueue(1)
        iq.enqueue(2)
        expected = "[1, 2]"
        self.assertEqual(str(iq), expected)

# def main():
#     unittest.main()



def friend_link(friends, person_A: str, person_B: str):
    # use a set to record all people that have been reached
    # to avoid infinite loop
    reached = set()
    return dfs(person_A, person_B, friends, reached)


def dfs(cur_person, destination, friends, reached):
    # base case 1: found the destination person
    if cur_person == destination:
        return True
    # base case 2: already checked the current person
    if cur_person in reached:
        return False
    
    # mark the person as reached 
    reached.add(cur_person)
    # loop the all friends cur_person has, to see if there is a link
    # if 1 link exists, return True
    # if no such link, return False 
    for next_person in friends[cur_person]:
        if dfs(next_person, destination, friends, reached):
            return True
    return False


def main():
    friends = {
    "Cat": {"Elephant", "Rasika"},
    "Dog": {"Elephant", "Giraffe", "Cat"},
    "Rasika": {"Cat", "Elephant"},
    "Elephant": {"Giraffe", "Rasika"},
    "Giraffe": set()
    }
    print(friend_link(friends, "Giraffe", "Cat"))
    print(friend_link(friends, "Dog", "Dog"))

main()





