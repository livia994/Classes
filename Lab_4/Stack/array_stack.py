from abstract_stack import AbstractStack

class ArrayStack(AbstractStack):
    def __init__(self, capacity=5):
        self.stack = [None] * capacity
        self.size = 0

    def push(self, item):
        if not self.is_full():
            self.stack[self.size] = item
            self.size += 1
        else:
            print("Stack is full. Cannot push element.")

    def pop(self):
        if not self.is_empty():
            self.size -= 1
            return self.stack[self.size]

    def top(self):
        if not self.is_empty():
            return self.stack[self.size - 1]

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == len(self.stack)
