# Quan, Yuan
# Dec 4, 2022

# ADT Stack: data structure that is ordered (like list)
# Can only add and remove from the end, check if empty
# push, pop
# Last in, first out (LIFO)

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop from empty stack.")
        item = self.items[-1]
        self.items = self.items[:-1]
        return item
    
    def is_empty(self):
        return len(self.items) == 0
    
    def __str__(self):
        return str(self.items)