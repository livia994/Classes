import os
import datetime

class Document:
    def __init__(self, name, path, extension):
        self.name = name
        self.path = path
        self.extension = extension
        self.created_time = datetime.datetime.now()
        self.updated_time = self.created_time
        self.changes = []
    def update(self, change_details, change_type):
        self.updated_time = datetime.datetime.now()
        self.changes.append((self.updated_time, change_details, change_type))
    def info(self):
        print(f"Name: {self.name}")
        print(f"Extension: {self.extension}")
        print(f"Created Time: {self.created_time}")
        print(f"Updated Time: {self.updated_time}")

        if self.changes:
            print("Changes:")
            for time, change, change_type in self.changes:
                print(f"- {time}: {change_type} - {change}")
        else:
            print("No changes.")
    def has_changed(self, snapshot_time):
        return self.updated_time > snapshot_time

class TextDocument(Document):
    def __init__(self, name, path):
        super().__init__(name, path, 'txt')
        self.line_count = 0
        self.word_count = 0
        self.character_count = 0
        self.change_history = []

    def update_counts(self, change_details):
        if os.path.exists(self.path):
            with open(self.path, 'r') as file:
                lines = file.readlines()
                self.line_count = len(lines)
                self.word_count = sum(len(line.split()) for line in lines)
                self.character_count = sum(len(line) for line in lines)
                self.change_history.append((datetime.datetime.now(), change_details))
        else:
            print(f"File not found: {self.path}")

    def info(self):
        super().info()
        self.update_counts("Text change details")
        print(f"Line Count: {self.line_count}")
        print(f"Word Count: {self.word_count}")
        print(f"Character Count: {self.character_count}")

        if self.change_history:
            print("Text Changes:")
            for time, change in self.change_history:
                print(f"- {time}: {change}")
        else:
            print("No text changes.")

    def commit(self, message, change_type):
        super().update(message, change_type)

class ImageDocument(Document):
    def __init__(self, name, path):
        super().__init__(name, path, 'png')
        self.image_size = (0, 0)
        self.image_changes = []

    def update_size(self):
        pass

    def commit(self, message):
        self.update(message, "Image Change")

    def info(self):
        super().info()
        print(f"Image Size: {self.image_size[0]}x{self.image_size[1]}")
        if self.image_changes:
            print("Image Changes:")
            for time, change in self.image_changes:
                print(f"- {time}: {change}")
        else:
            print("No image changes.")

class ProgramDocument(Document):
    def __init__(self, name, path):
        super().__init__(name, path, 'py')
        self.line_count = 0
        self.class_count = 0
        self.method_count = 0

    def update_counts(self):
        with open(self.path, 'r') as file:
            lines = file.readlines()
            self.line_count = len(lines)
            self.count_classes_and_methods(lines)

    def count_classes_and_methods(self, lines):
        self.class_count = sum(1 for line in lines if 'class ' in line)
        self.method_count = sum(1 for line in lines if line.strip().startswith('def '))
    def info(self):
        super().info()
        self.update_counts()
        print(f"Line Count: {self.line_count}")
        print(f"Class Count: {self.class_count}")
        print(f"Method Count: {self.method_count}")



class DocumentManager:
    def __init__(self):
        self.documents = {}
        self.snapshot_time = datetime.datetime.now()

    def commit(self):
        self.snapshot_time = datetime.datetime.now()
        for document in self.documents.values():
            document.update("Snapshot", "Snapshot")

    def add_document(self, path=None):
        if path:
            name, ext = os.path.splitext(os.path.basename(path))
            ext = ext[1:]
            if ext == 'txt':
                doc = TextDocument(name, path)
            elif ext == 'png':
                doc = ImageDocument(name, path)
            elif ext == 'py':
                doc = ProgramDocument(name, path)
            else:
                doc = Document(name, path, ext)
                doc.created_time = datetime.datetime.fromtimestamp(os.path.getctime(path))
            self.documents[name] = doc
        else:
            pass

    def commit(self, filename, message, change_type):
        if filename in self.documents:
            document = self.documents[filename]
            document.update(message, change_type)
        else:
            print(f"File not found: {filename}")
    def status(self):
        print(f"Created Snapshot at: {self.snapshot_time}")
        for name, document in self.documents.items():
            if document.has_changed(self.snapshot_time):
                print(f"{name}.{document.extension} - Changed")
            else:
                print(f"{name}.{document.extension} - NoChange")
            document.info()

