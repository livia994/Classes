from abstract_queue import AbstractQueue

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedQueue(AbstractQueue):
    def __init__(self):
        self.front_node = None
        self.rear_node = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front_node = self.rear_node = new_node
        else:
            self.rear_node.next = new_node
            self.rear_node = new_node

    def dequeue(self):
        if not self.is_empty():
            item = self.front_node.data
            self.front_node = self.front_node.next
            if self.front_node is None:
                self.rear_node = None
            return item

    def front(self):
        if not self.is_empty():
            return self.front_node.data

    def is_empty(self):
        return self.front_node is None

    def is_full(self):
        return False
