import os
import datetime

class Document:
    def __init__(self, name, path, extension):
        self.name = name
        self.path = path
        self.extension = extension
        self.created_time = datetime.datetime.now()
        self.updated_time = datetime.datetime.now()

    def update(self):
        self.updated_time = datetime.datetime.now()

    def info(self):
        print(f"Name: {self.name}")
        print(f"Extension: {self.extension}")
        print(f"Created Time: {self.created_time}")
        print(f"Updated Time: {self.updated_time}")

    def has_changed(self, snapshot_time):
        return self.updated_time > snapshot_time

class TextDocument(Document):
    def __init__(self, name, path):
        super().__init__(name, path, 'txt')
        self.line_count = 0
        self.word_count = 0
        self.character_count = 0

    def update_counts(self):
        with open(self.path, 'r') as file:
            lines = file.readlines()
            self.line_count = len(lines)
            self.word_count = sum(len(line.split()) for line in lines)
            self.character_count = sum(len(line) for line in lines)

    def info(self):
        super().info()
        print(f"Line Count: {self.line_count}")
        print(f"Word Count: {self.word_count}")
        print(f"Character Count: {self.character_count}")

class ImageDocument(Document):
    def __init__(self, name, path):
        super().__init__(name, path, 'png')
        self.image_size = (0, 0)

    def update_size(self):
        pass

    def info(self):
        super().info()
        print(f"Image Size: {self.image_size[0]}x{self.image_size[1]}")

class ProgramDocument(Document):
    def __init__(self, name, path):
        super().__init__(name, path, 'py')
        self.line_count = 0
        self.class_count = 0
        self.method_count = 0

    def update_counts(self):
        pass

    def info(self):
        super().info()
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
            document.update()

    def add_document(self, path):
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
        self.documents[name] = doc

    def status(self):
        print(f"Created Snapshot at: {self.snapshot_time}")
        for name, document in self.documents.items():
            if document.has_changed(self.snapshot_time):
                print(f"{name}.{document.extension} - Changed")
            else:
                print(f"{name}.{document.extension} - NoChange")

