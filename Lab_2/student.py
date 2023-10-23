from enum import Enum


class StudyField(Enum):
    MECHANICAL_ENGINEERING = 1
    SOFTWARE_ENGINEERING = 2
    FOOD_TECHNOLOGY = 3
    URBANISM_ARCHITECTURE = 4
    VETERINARY_MEDICINE = 5


class Student:

    def __init__(self, first_name, last_name, email, enrollment_date, date_of_birth, faculty):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.enrollment_date = enrollment_date
        self.date_of_birth = date_of_birth
        self.faculty = faculty
        self.is_graduated = False

    def graduate(self):

        self.is_graduated = True

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def generate_abbreviation(self, field):
        words = field.split("_")
        abbreviation = "".join(word[:2].upper() for word in words[:2])
        return abbreviation