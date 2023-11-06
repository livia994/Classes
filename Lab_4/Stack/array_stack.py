from abc import ABC, abstractmethod

class AbstractStack(ABC):
    @abstractmethod
    def push(self, item):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def top(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass

class ArrayStack(AbstractStack):
    def __init__(self, capacity=10):
        self.stack = [None] * capacity
        self.size = 0

    def push(self, item):
        if self.size == len(self.stack):
            self._resize()
        self.stack[self.size] = item
        self.size += 1

    def pop(self):
        if not self.is_empty():
            self.size -= 1
            return self.stack[self.size]

    def top(self):
        if not self.is_empty():
            return self.stack[self.size - 1]

    def is_empty(self):
        return self.size == 0

    def _resize(self):
        new_stack = [None] * (2 * len(self.stack))
        for i in range(self.size):
            new_stack[i] = self.stack[i]
        self.stack = new_stack