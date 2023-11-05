from list_stack import ListStack
from linked_stack import LinkedStack
from array_stack import ArrayStack
def test_list_stack():
    stack = ListStack()

    print("Is the stack empty?", stack.is_empty())

    stack.push(1)
    stack.push(2)
    stack.push(3)

    print("Top element:", stack.top())

    popped = stack.pop()
    print("Popped element:", popped)
    print("Is the stack empty?", stack.is_empty())

    while not stack.is_empty():
        print("Popped element:", stack.pop())

def test_linked_stack():
    stack = LinkedStack()

    print("Is the linked stack empty?", stack.is_empty())

    stack.push(1)
    stack.push(2)
    stack.push(3)

    print("Top element:", stack.top())

    popped = stack.pop()
    print("Popped element:", popped)
    print("Is the linked stack empty?", stack.is_empty())

    while not stack.is_empty():
        print("Popped element:", stack.pop())

def test_array_stack():
    stack = ArrayStack()

    print("Is the array stack empty?", stack.is_empty())

    stack.push(1)
    stack.push(2)
    stack.push(3)

    print("Top element:", stack.top())

    popped = stack.pop()
    print("Popped element:", popped)
    print("Is the array stack empty?", stack.is_empty())

    while not stack.is_empty():
        print("Popped element:", stack.pop())

if __name__ == "__main__":
    test_list_stack()
    test_linked_stack()
    test_array_stack()
