from enum import Enum


class StudyField(Enum):
    MECHANICAL_ENGINEERING = 1
    SOFTWARE_ENGINEERING = 2
    FOOD_TECHNOLOGY = 3
    URBANISM_ARCHITECTURE = 4
    VETERINARY_MEDICINE = 5


class Student:

    def __init__(self, first_name, last_name, email, enrollment_date, date_of_birth, faculty):
        self.first_name = first_name  # Student's first name
        self.last_name = last_name    # Student's last name
        self.email = email            # Student's email
        self.enrollment_date = enrollment_date  # Enrollment date (YYYY-MM-DD)
        self.date_of_birth = date_of_birth
        self.faculty = faculty        # Faculty to which the student belongs
        self.is_graduated = False     # Student's graduation status (default is False)

    def graduate(self):
        # Mark the student as graduated
        self.is_graduated = True

    def __str__(self):
        # String representation of the student
        return f"{self.first_name} {self.last_name} ({self.student_id})"

    def generate_abbreviation(self, field):
        # Convert the first two words of the field name to uppercase and concatenate them
        words = field.split("_")
        abbreviation = "".join(word[:2].upper() for word in words[:2])
        return abbreviation