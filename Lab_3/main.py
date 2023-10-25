import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from document import DocumentManager, TextDocument, ImageDocument

class MyHandler(FileSystemEventHandler):
    def __init__(self, app):
        super(MyHandler, self).__init__()
        self.app = app

    def on_created(self, event):
        if event.is_directory:
            return
        filename = os.path.basename(event.src_path)
        self.app.add_file(filename)
        print(f"File added: {filename}")

    def on_deleted(self, event):
        if event.is_directory:
            return
        filename = os.path.basename(event.src_path)
        self.app.remove_file(filename)
        print(f"File removed: {filename}")

class DocumentManagerApp:
    def __init__(self, folder_path):
        self.manager = DocumentManager()
        self.folder_path = folder_path
        self.event_handler = MyHandler(self)
        self.observer = Observer()
        self.observer.schedule(self.event_handler, path=folder_path, recursive=False)
        self.observer.start()

    def add_file(self, file_to_add):
        file_path = os.path.join(self.folder_path, file_to_add)
        if os.path.exists(file_path):
            if file_to_add.endswith('.png'):
                doc = ImageDocument(file_to_add, file_path)
            else:
                doc = TextDocument(file_to_add, file_path)
            self.manager.add_document(file_path)
            print(f"Added {file_to_add} for monitoring.")
        else:
            print(f"File not found: {file_to_add}")

    def remove_file(self, file_to_remove):
        if file_to_remove in self.manager.documents:
            del self.manager.documents[file_to_remove]
            print(f"Removed {file_to_remove} from monitoring.")
        else:
            print(f"File not found: {file_to_remove}")

    def run(self):
        try:
            while True:
                command = input("Enter a command (commit <filename> <message>, info <filename>, status, add <filename>): ").split()
                if command[0] == "commit":
                    filename = input("Enter the filename you want to commit changes for: ")
                    message = input("Enter a commit message: ")
                    if filename in self.manager.documents:
                        self.manager.commit(filename, message, "Text Change")
                    else:
                        print(f"File not found: {filename}")
                elif command[0] == "info" and len(command) == 2:
                    filename = command[1]
                    if filename in self.manager.documents:
                        self.manager.documents[filename].info()
                    else:
                        print("File not found.")
                elif command[0] == "status":
                    self.manager.status()
                elif command[0] == "add" and len(command) == 2:
                    file_to_add = command[1]
                    self.add_file(file_to_add)
                else:
                    print("Invalid command. Try again.")
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()

if __name__ == "__main__":
    folder_path = "C:/Users/olivi/OneDrive/Desktop/Lab #3 OOP"
    app = DocumentManagerApp(folder_path)
    app.run()
