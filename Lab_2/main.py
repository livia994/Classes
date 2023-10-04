from student import Student
from Lab_2.faculty import Faculty
from university import University
from student import StudyField

def main_menu():
    university = University()

    university.add_faculty("Faculty of Mechanical Engineering", "ME", StudyField.MECHANICAL_ENGINEERING)
    university.add_faculty("Faculty of Software Engineering", "SE", StudyField.SOFTWARE_ENGINEERING)
    university.add_faculty("Faculty of Food Technology", "FT", StudyField.FOOD_TECHNOLOGY)
    university.create_faculty("Faculty of Veterinary Medicine", StudyField.VETERINARY_MEDICINE, "VM")

    while True:
        print("\nWelcome to TUM's student management system!")
        print("What do you want to do?")
        print("g - General operations")
        print("f - Faculty operations")
        print("s - Student operations")
        print("q - Quit program")

        choice = input("Your input> ")

        if choice == "g":
            general_operations(university)
        elif choice == "f":
            faculty_operations(university)
        elif choice == "s":
            student_operations(university)
        elif choice == "q":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

def general_operations(university):
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
            create_new_faculty(university)
        elif choice == "2":
            search_student_faculty(university)
        elif choice == "3":
            display_university_faculties(university)
        elif choice == "4":
            display_faculties_by_field(university)
        elif choice == "b":
            break
        elif choice == "q":
            print("Exiting the program.")
            exit()
        else:
            print("Invalid choice. Please select a valid option.")

def create_new_faculty(university):
    faculty_name = input("Enter faculty name: ")
    study_field = input("Enter study field (e.g., MECHANICAL_ENGINEERING): ")
    abbreviation = input("Enter abbreviation: ")
    university.create_faculty(faculty_name, study_field, abbreviation)
    print(f"Faculty '{faculty_name}' created.")

def search_student_faculty(university):
    student_email = input("Enter student email: ")
    faculty_name = university.find_faculty_by_student_email(student_email)
    if faculty_name != "Student not found in any faculty.":
        print(f"The student belongs to '{faculty_name}' faculty.")
    else:
        print("Student not found in any faculty.")


def display_university_faculties(university):
    print("University Faculties:")
    faculties = university.display_all_faculties()
    if faculties:
        for faculty in faculties:
            print(faculty)
    else:
        print("No faculties in the university.")


def display_faculties_by_field(university):
    field = input("Enter the field to display faculties (e.g., FOOD_TECHNOLOGY): ")
    faculties = university.display_faculties_by_field(field)
    if faculties:
        print(f"Faculties in the field of {field}:")
        for faculty in faculties:
            print(faculty)
    else:
        print(f"No faculties found in the field of {field}.")


def faculty_operations(university):
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
            create_and_assign_student(university)
        elif choice == "2":
            graduate_student(university)
        elif choice == "3":
            display_enrolled_students(university)
        elif choice == "4":
            display_graduates(university)
        elif choice == "5":
            check_student_faculty(university)
        elif choice == "b":
            break
        elif choice == "q":
            print("Exiting the program.")
            exit()
        else:
            print("Invalid choice. Please select a valid option.")
def student_operations(university):
    while True:
        print("\nStudent Operations Menu:")
        print("1. Add a student to a faculty")
        print("2. Search for a student's faculty")
        print("3. Display all university faculties")
        print("4. Display faculties by field")
        print("b - Back")
        print("q - Quit program")

        choice = input("Your input> ")

        if choice == "1":
            create_and_assign_student(university)
        elif choice == "2":
            search_student_faculty(university)
        elif choice == "3":
            display_university_faculties(university)
        elif choice == "4":
            display_faculties_by_field(university)
        elif choice == "b":
            break
        elif choice == "q":
            print("Exiting the program.")
            exit()
        else:
            print("Invalid choice. Please select a valid option.")

def create_and_assign_student(university):
    print("Enter student information:")
    email = input("Email: ")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    birthdate = input("Birthdate (month/day/year): ")

    print("Choose the faculty to assign the student:")
    for faculty in university.faculties:
        print(f"{faculty.abbreviation} - {faculty.faculty_name}")

    faculty_abbreviation = input("Enter the faculty abbreviation: ")

    # Search for the matching faculty by abbreviation
    matching_faculty = Faculty.find_faculty_by_abbreviation(university.faculties, faculty_abbreviation)

    if matching_faculty:
        student_info = f"nf/{faculty_abbreviation}/{matching_faculty.faculty_name}/{first_name}/{last_name}/{email}/{birthdate}"
        print(f"Student was successfully added: {student_info}")

        # Create and assign the student to the matching faculty
        student = Student(first_name, last_name, email, birthdate, faculty, matching_faculty)
        # Pass faculty directly
        matching_faculty.add_student(student)
        print(f"Student '{first_name} {last_name}' assigned to {matching_faculty.faculty_name} faculty.")
    else:
        print(f"Faculty with abbreviation '{faculty_abbreviation}' not found.")




def graduate_student(university):
    student_email = input("Enter student email: ")
    result = university.graduate_student(student_email)
    print(result)


def display_enrolled_students(university):
    enrolled_students = university.display_enrolled_students()
    if enrolled_students:
        print("Enrolled Students:")
        print(enrolled_students)
    else:
        print("No enrolled students in any faculty.")


def display_graduates(university):
    graduated_students = university.display_graduates()
    if graduated_students:
        print("Graduated Students:")
        print(graduated_students)
    else:
        print("No graduates from any faculty.")


def check_student_faculty(university):
    student_email = input("Enter student email: ")
    faculty_name = university.find_faculty_by_student_email(student_email)
    if faculty_name != "Student not found in any faculty.":
        print(f"Yes, the student belongs to '{faculty_name}' faculty.")
    else:
        print("No, the student does not belong to any faculty.")


if __name__ == "__main__":
    main_menu()
