import os
from document import DocumentManager, TextDocument, ImageDocument

current_directory = os.getcwd()
folder_name = "Lab #3 OOP"

folder_path = os.path.join("C:/Users/olivi/OneDrive/Desktop/Lab #3 OOP")

if __name__ == "__main__":
    manager = DocumentManager()

    while True:
        command = input("Enter a command (commit <filename> <message>, info <filename>, status, add <filename>): ").split()
        if command[0] == "commit":
            filename = input("Enter the filename you want to commit changes for: ")
            message = input("Enter a commit message: ")
            if filename.endswith('.png'):
                document = ImageDocument(filename, os.path.join(folder_path, filename))
                document.commit(message, "Image Change")
            else:
                document = TextDocument(filename, os.path.join(folder_path, filename))
                document.commit(message, "Text Change")
        elif command[0] == "info" and len(command) == 2:
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
                if file_to_add.endswith('.png'):
                    doc = ImageDocument(file_to_add, file_path)
                else:
                    doc = TextDocument(file_to_add, file_path)
                manager.add_document(doc)
                print(f"Added {file_to_add} for monitoring.")
            else:
                print(f"File not found: {file_to_add}")
        else:
            print("Invalid command. Try again.")
