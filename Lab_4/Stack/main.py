from list_stack import ListStack
from linked_stack import LinkedStack
from array_stack import ArrayStack


def main():
    print("Select data structure:")
    print("1. Stack")
    print("2. Queue")
    choice = input("Enter 1 for Stack or 2 for Queue: ")

    if choice == '1':
        print("Select Stack implementation:")
        print("1. List Stack")
        print("2. Linked Stack")
        print("3. Array Stack")
        stack_choice = input("Enter 1, 2, or 3: ")

        if stack_choice == '1':
            stack = ListStack()
        elif stack_choice == '2':
            stack = LinkedStack()
        elif stack_choice == '3':
            stack = ArrayStack()
        else:
            print("Invalid choice for Stack implementation.")
            return

        stack_operations(stack)


def stack_operations(stack):
    while True:
        print("Stack Operations:")
        print("1. Push")
        print("2. Pop")
        print("3. Top")
        print("4. Check if Stack is empty")
        print("5. Exit")
        operation = input("Enter 1, 2, 3, 4, or 5: ")

        if operation == '1':
            item = input("Enter item to push: ")
            stack.push(item)
        elif operation == '2':
            popped_item = stack.pop()
            if popped_item is not None:
                print(f"Popped item: {popped_item}")
            else:
                print("Stack is empty.")
        elif operation == '3':
            top_item = stack.top()
            if top_item is not None:
                print(f"Top item: {top_item}")
            else:
                print("Stack is empty.")
        elif operation == '4':
            if stack.is_empty():
                print("Stack is empty.")
            else:
                print("Stack is not empty.")
        elif operation == '5':
            break
        else:
            print("Invalid operation choice.")


if __name__ == "__main__":
    main()
