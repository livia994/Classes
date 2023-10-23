from Lab_2.faculty import Faculty
from Lab_2.student import Student
from Lab_2.student import StudyField

class University:
    def __init__(self):
        self.faculties = []
        self.faculties_by_field = {field: [] for field in StudyField}
        self.initialize_faculties()

    def initialize_faculties(self):
        faculties_data = [
            ("Faculty of Mechanical Engineering", "ME", StudyField.MECHANICAL_ENGINEERING),
            ("Faculty of Software Engineering", "SE", StudyField.SOFTWARE_ENGINEERING),
            ("Faculty of Food Technology", "FT", StudyField.FOOD_TECHNOLOGY),
            ("Faculty of Veterinary Medicine", "VM", StudyField.VETERINARY_MEDICINE),
        ]

        for faculty_data in faculties_data:
            faculty_name, abbreviation, field = faculty_data
            self.add_faculty(faculty_name, abbreviation, field)

    def add_faculty(self, faculty_name, abbreviation, field):
            faculty = Faculty(faculty_name, abbreviation, field)
            self.faculties.append(faculty)

    def get_faculties_by_field(self, study_field):
        return self.faculties_by_field.get(study_field, [])
    def create_faculty(self, faculty_name, field, abbreviation):
        faculty = Faculty(faculty_name, field, abbreviation)
        self.faculties.append(faculty)

    def assign_student_to_faculty(self, student_first_name, student_last_name, student_email, enrollment_date, date_of_birth, faculty_abbreviation):
        for faculty in self.faculties:
            if faculty.abbreviation == faculty_abbreviation:
                student = Student(student_first_name, student_last_name, student_email, enrollment_date, date_of_birth, faculty)
                faculty.add_student(student)
                return f"{student.first_name} assigned to {faculty.faculty_name}."
        return f"Faculty with abbreviation {faculty_abbreviation} not found."

    def graduate_student(self, student_email):
        for faculty in self.faculties:
            result = faculty.graduate_student(student_email)
            if not result.startswith("Student with email"):
                return result
        return f"Student with email {student_email} not found in any faculty."
# TODO data de absolvire sa fie displayed cand se afiseaza lista de absolventi - sa se ia in considerare data de azi
    def display_enrolled_students(self):
        enrolled_students = [student for faculty in self.faculties for student in faculty.get_enrolled_students()]
        return "\n".join([f"{student.first_name} {student.last_name} - {student.faculty.faculty_name}" for student in enrolled_students])

    def display_graduates(self):
        graduated_students = [student for faculty in self.faculties for student in faculty.get_graduates()]
        return "\n".join([f"{student.first_name} {student.last_name} - {student.faculty.faculty_name}" for student in graduated_students])

    def find_faculty_by_student_email(self, student_email):
        for faculty in self.faculties:
            if faculty.is_student_enrolled(student_email):
                return faculty.faculty_name
        return "Student not found in any faculty."

    def display_all_faculties(self):
        return [str(faculty) for faculty in self.faculties]

    def display_faculties_by_field(self, field):
        field = field.upper()
        valid_fields = [
            "MECHANICAL_ENGINEERING", "SOFTWARE_ENGINEERING", "FOOD_TECHNOLOGY",
            "URBANISM_ARCHITECTURE", "VETERINARY_MEDICINE"
        ]
        if field in valid_fields:
            return [str(faculty) for faculty in self.faculties if faculty.study_field == field]
        else:
            return []

    def __str__(self):
        return "University"
    def __getstate__(self):
        return self.__dict__

    def __setstate__(self, state):
        self.__dict__.update(state)