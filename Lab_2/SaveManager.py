import pickle

class SaveManager:
    def __init__(self, filename):
        self.filename = filename

    def save(self, data):
        try:
            with open(self.filename, 'wb') as file:
                pickle.dump(data, file)
            print("Data saved successfully!")
        except Exception as e:
            print("Error saving data:", str(e))

    def load(self):
        try:
            with open(self.filename, 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            return None