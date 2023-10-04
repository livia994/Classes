import pickle

class SaveManager:
    def __init__(self, filename):
        self.filename = filename

    def save(self, data):
        with open(self.filename, 'wb') as file:
            pickle.dump(data, file)

    def load(self):
        try:
            with open(self.filename, 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            return None