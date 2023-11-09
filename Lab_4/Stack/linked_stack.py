from abstract_stack import AbstractStack

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedStack(AbstractStack):
    def __init__(self):
        self.top_node = None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top_node
        self.top_node = new_node

    def pop(self):
        if not self.is_empty():
            item = self.top_node.data
            self.top_node = self.top_node.next
            return item

    def top(self):
        if not self.is_empty():
            return self.top_node.data

    def is_empty(self):
        return self.top_node is None

    def is_full(self):
        return False  # LinkedStack is not restricted by capacity
