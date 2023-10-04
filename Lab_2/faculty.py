from student import StudyField

class Faculty:
    def __init__(self, faculty_name, study_field, abbreviation):
        self.faculty_name = faculty_name
        self.study_field = study_field
        self.abbreviation = abbreviation
        self.students_list = []
        self.graduates = []

    def add_student(self, student):
        self.students_list.append(student)

    def graduate_student(self, student_email):
        for student in self.students_list:
            if student.email == student_email:
                graduated_student = self.students_list.pop(self.students_list.index(student))
                graduated_student.is_graduated = True
                self.graduates.append(graduated_student)
                return f"{graduated_student.first_name} {graduated_student.last_name} has graduated."
        return f"Student with email {student_email} not found in {self.faculty_name}."

    def get_enrolled_students(self):
        return [student for student in self.students_list if not student.is_graduated]

    def get_graduates(self):
        return [student for student in self.graduates if student.is_graduated]


    def is_student_enrolled(self, student_email):
        return any(student.email == student_email for student in self.students_list)

    def find_faculty_by_abbreviation(faculties, abbreviation):
        for faculty in faculties:
            if faculty.abbreviation == abbreviation:
                return faculty
        return None
    def __str__(self):
        return f"{self.faculty_name} ({self.abbreviation})"
