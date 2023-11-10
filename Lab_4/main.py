from Stack.list_stack import ListStack
from Stack.linked_stack import LinkedStack
from Stack.array_stack import ArrayStack
from Queue.array_up_queue import ArrayUpQueue
from Queue.LinkedQueue import LinkedQueue
from Queue.ListQueue import ListQueue

class DataStructureManager:
    def __init__(self):
        pass

    def main(self):
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

            self.stack_operations(stack)

        elif choice == '2':
            print("Select Queue implementation:")
            print("1. List Queue")
            print("2. Linked Queue")
            print("3. Array Up Queue")
            queue_choice = input("Enter 1, 2, or 3: ")

            if queue_choice == '1':
                queue = ListQueue()
            elif queue_choice == '2':
                queue = LinkedQueue()
            elif queue_choice == '3':
                queue = ArrayUpQueue()
            else:
                print("Invalid choice for Queue implementation.")
                return

            self.queue_operations(queue)

        else:
            print("Invalid choice for data structure.")

    def stack_operations(self, stack):
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

    def queue_operations(self, queue):
        while True:
            print("Queue Operations:")
            print("1. Enqueue")
            print("2. Dequeue")
            print("3. Front")
            print("4. Check if Queue is empty")
            print("5. Exit")
            operation = input("Enter 1, 2, 3, 4, or 5: ")

            if operation == '1':
                item = input("Enter item to enqueue: ")
                queue.enqueue(item)
            elif operation == '2':
                dequeued_item = queue.dequeue()
                if dequeued_item is not None:
                    print(f"Dequeued item: {dequeued_item}")
                else:
                    print("Queue is empty.")
            elif operation == '3':
                front_item = queue.front()
                if front_item is not None:
                    print(f"Front item: {front_item}")
                else:
                    print("Queue is empty.")
            elif operation == '4':
                if queue.is_empty():
                    print("Queue is empty.")
                else:
                    print("Queue is not empty.")
            elif operation == '5':
                break
            else:
                print("Invalid operation choice.")

if __name__ == "__main__":
    manager = DataStructureManager()
    manager.main()
