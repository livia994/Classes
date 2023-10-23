import os
from document import DocumentManager

if __name__ == "__main__":
    manager = DocumentManager()
    folder_path = "your_folder_path"

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            manager.add_document(file_path)

    while True:
        command = input("Enter a command (commit, info <filename>, status): ").split()
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
        else:
            print("Invalid command. Try again.")
