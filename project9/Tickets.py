# Quan, Yuan
# Dec 4, 2022
# this program mimic a ticket line where people are being served one by one, and more people are joining the back of the line

from Queue import Queue
import random

# this function pick a random number form 0,1,2 and add corresponding customers in the line
# parameter: a Queue of int (line of customers), total people entered
# return: total people entered after new joiners
def new_joiner(ticket_line, people_entered):
    newjoiners = random.randint(0,2)
    for i in range(newjoiners):
        ticket_line.enqueue(people_entered+i)
    people_entered += newjoiners
    return people_entered


# this function serve 1 customer at the top of the line if the line is not empty
# parameter: a Queue of int (line of customers), total people served
# print: customer X is surved, where X is the number of customer
# return: total people served after this one
def serve(ticket_line, people_served):
    if ticket_line.is_empty():
        return people_served
    customer = ticket_line.dequeue()
    print(f"cumtomer {customer} is served")
    people_served += 1
    return people_served


# the flow is to iterate for 100 times
# each time random decide whether 0,1,or 2 people join the line
# and serve only 1 people
# at the end, decide how many people are still in the line
def main():
    ticket_line = Queue()
    people_entered = 0
    people_served = 0
    for _ in range(100):
        people_entered = new_joiner(ticket_line, people_entered)
        people_served = serve(ticket_line, people_served)
    
    people_left = people_entered - people_served
    print(f"There are still {people_left} people in the line.")


if __name__ == "__main__":
    main()
