import os
from document import DocumentManager
current_directory = os.getcwd()

folder_name = "Lab #3 OOP"

folder_path = os.path.join(current_directory, folder_name)
if __name__ == "__main__":
    manager = DocumentManager()
    folder_path = "your_absolute_path_to_Lab_3_OOP"

    while True:
        command = input("Enter a command (commit, info <filename>, status, add <filename>): ").split()
        if command[0] == "commit":
            manager.commit()
        elif command[0] == "info":
            if len(command) == 2:
                filename = command[1]
                if filename in manager.documents:
                    manager.documents[filename].info()
                else:
                    print("File not found.")
        elif command[0] == "status":
            manager.status()
        elif command[0] == "add" and len(command) == 2:
            file_to_add = command[1]
            file_path = os.path.join(folder_path, file_to_add)
            if os.path.exists(file_path):
                manager.add_document(file_path)
                print(f"Added {file_to_add} for monitoring.")
            else:
                print(f"File not found: {file_to_add}")
        else:
            print("Invalid command. Try again.")
