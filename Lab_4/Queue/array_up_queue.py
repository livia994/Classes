from abstract_queue import AbstractQueue

class ArrayUpQueue(AbstractQueue):
    def __init__(self, capacity=5):
        self.queue = [None] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0

    def enqueue(self, item):
        if not self.is_full():
            self.queue[self.rear] = item
            self.rear = (self.rear + 1) % len(self.queue)
            self.size += 1
        else:
            print("Queue is full. Cannot enqueue element.")

    def dequeue(self):
        if not self.is_empty():
            item = self.queue[self.front]
            self.front = (self.front + 1) % len(self.queue)
            self.size -= 1
            return item

    def front(self):
        if not self.is_empty():
            return self.queue[self.front]

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == len(self.queue) 