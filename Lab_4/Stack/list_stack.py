from abstract_stack import AbstractStack

class ListStack(AbstractStack):
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def top(self):
        if not self.is_empty():
            return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return False  # ListStack is not restricted by capacity
