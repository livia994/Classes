from collections import deque

class ListQueue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()

    def front(self):
        if not self.is_empty():
            return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0
