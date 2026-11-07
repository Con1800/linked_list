class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    
    # O(n) linear time
    def __len__(self):
        return self.size

    def __repr__(self):
        pass

    def push(self, value):
        pass

    def pop(self):
        pass

    def peek(self):
        pass

    def is_empty(self):
        return self.top is None