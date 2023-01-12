# Quan, Yuan
# Dec 4, 2022

# ADT Queue: data structure that is ordered (like list)
# can only add to one end, and remove from the other end, check if empty
# enqueue, dequeue
# First in, first out (FIFO)

class Queue:
    def __init__(self, list = []):
        self.items = list
    
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Cannot dequeue from empty queue")
        item = self.items[0]
        self.items = self.items[1:]
        return item

    def is_empty(self):
        return len(self.items)==0

    # not used in main project, but for tests.
    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)
