from list_stack import ListStack

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

if __name__ == "__main__":
    test_list_stack()
