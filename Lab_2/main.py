from student import Student
from faculty import Faculty
from university import University
from student import StudyField
from SaveManager import SaveManager
from sys import exit
import os
class UniversitySystem:
    def __init__(self):
        self.save_manager = SaveManager("university_data.pkl")
        self.university = self.initialize_university()

    def initialize_university(self):
        if os.path.exists("university_data.pkl"):
            os.remove("university_data.pkl")

        university = self.save_manager.load()

        if university is None:
            university = University()
            university.initialize_faculties()

        return university

    def main_menu(self):
        while True:
            print("\nWelcome to TUM's student management system!")
            print("What do you want to do?")
            print("g - General operations")
            print("f - Faculty operations")
            print("s - Student operations")
            print("q - Quit program")

            choice = input("Your input> ")

            if choice == "g":
                self.general_operations()
            elif choice == "f":
                self.faculty_operations()
            elif choice == "s":
                self.student_operations()
            elif choice == "q":
                print("Exiting the program.")
                self.save_manager.save(self.university)
                break
            else:
                print("Invalid choice. Please select a valid option.")

    def general_operations(self):
        while True:
            print("\nGeneral Operations Menu:")
            print("1. Create a new faculty")
            print("2. Search what faculty a student belongs to by email")
            print("3. Display all university faculties")
            print("4. Display faculties by field")
            print("b - Back")
            print("q - Quit program")

            choice = input("Your input> ")

            if choice == "1":
                self.create_new_faculty()
            elif choice == "2":
                self.search_student_faculty()
            elif choice == "3":
                self.display_university_faculties()
            elif choice == "4":
                self.display_faculties_by_field()
            elif choice == "b":
                break
            elif choice == "q":
                print("Exiting the program.")
                exit()
            else:
                print("Invalid choice. Please select a valid option.")

    def create_new_faculty(self):
        faculty_name = input("Enter faculty name: ")
        study_field = input("Enter study field (e.g., MECHANICAL_ENGINEERING): ")
        abbreviation = input("Enter abbreviation: ")
        self.university.create_faculty(faculty_name, study_field, abbreviation)
        print(f"Faculty '{faculty_name}' created.")

    def search_student_faculty(self):
        student_email = input("Enter student email: ")
        faculty_name = self.university.find_faculty_by_student_email(student_email)
        if faculty_name != "Student not found in any faculty.":
            print(f"The student belongs to '{faculty_name}' faculty.")
        else:
            print("Student not found in any faculty.")

    def display_university_faculties(self):
        print("University Faculties:")
        faculties = self.university.display_all_faculties()
        if faculties:
            for faculty in faculties:
                print(faculty)
        else:
            print("No faculties in the university.")

    def display_faculties_by_field(self):
        field = input("Enter the field to display faculties (e.g., FOOD_TECHNOLOGY): ")
        faculties = self.university.display_faculties_by_field(field)
        if faculties:
            print(f"Faculties in the field of {field}:")
            for faculty in faculties:
                print(faculty)
        else:
            print(f"No faculties found in the field of {field}.")

    def faculty_operations(self):
        while True:
            print("\nFaculty Operations Menu:")
            print("1. Create and assign a student to a faculty")
            print("2. Graduate a student from a faculty")
            print("3. Display current enrolled students in faculties")
            print("4. Display graduates from faculties")
            print("5. Tell if a student belongs to a faculty")
            print("b - Back")
            print("q - Quit program")

            choice = input("Your input> ")

            if choice == "1":
                self.create_and_assign_student()
            elif choice == "2":
                self.graduate_student()
            elif choice == "3":
                self.display_enrolled_students()
            elif choice == "4":
                self.display_graduates()
            elif choice == "5":
                self.check_student_faculty()
            elif choice == "b":
                break
            elif choice == "q":
                print("Exiting the program.")
                exit()
            else:
                print("Invalid choice. Please select a valid option.")

    def create_and_assign_student(self):
        print("Enter student information:")
        email = input("Email: ")
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        birthdate = input("Birthdate (month/day/year): ")

        print("Choose the faculty to assign the student:")
        for faculty in self.university.faculties:
            print(f"{faculty.abbreviation} - {faculty.faculty_name}")

        faculty_abbreviation = input("Enter the faculty abbreviation: ")

        matching_faculty = Faculty.find_faculty_by_abbreviation(self.university.faculties, faculty_abbreviation)

        if matching_faculty:
            student_info = f"nf/{faculty_abbreviation}/{matching_faculty.faculty_name}/{first_name}/{last_name}/{email}/{birthdate}"
            print(f"Student was successfully added: {student_info}")

            student = Student(first_name, last_name, email, birthdate, matching_faculty.abbreviation, matching_faculty)
            matching_faculty.add_student(student)
            print(f"Student '{first_name} {last_name}' assigned to {matching_faculty.faculty_name} faculty.")
        else:
            print(f"Faculty with abbreviation '{faculty_abbreviation}' not found.")

    def graduate_student(self):
        student_email = input("Enter student email: ")
        result = self.university.graduate_student(student_email)
        print(result)

    def display_enrolled_students(self):
        enrolled_students = self.university.display_enrolled_students()
        if enrolled_students:
            print("Enrolled Students:")
            print(enrolled_students)
        else:
            print("No enrolled students in any faculty.")

    def display_graduates(self):
        graduated_students = self.university.display_graduates()
        if graduated_students:
            print("Graduated Students:")
            print(graduated_students)
        else:
            print("No graduates from any faculty.")

    def check_student_faculty(self):
        student_email = input("Enter student email: ")
        faculty_name = self.university.find_faculty_by_student_email(student_email)
        if faculty_name != "Student not found in any faculty.":
            print(f"Yes, the student belongs to '{faculty_name}' faculty.")
        else:
            print("No, the student does not belong to any faculty.")


if __name__ == "__main__":
    university_system = UniversitySystem()
    university_system.main_menu()
