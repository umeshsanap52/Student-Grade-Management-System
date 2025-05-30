class Student:
    def __init__(self, name, student_id, year, cgpa=0.0, attendance=0.0, grades=None):
        self.name = name
        self.student_id = student_id
        self.year = year
        self.cgpa = cgpa
        self.attendance = attendance
        self.grades = grades or []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0.0

    def update_cgpa(self, new_cgpa):
        self.cgpa = new_cgpa

    def update_attendance(self, new_attendance):
        self.attendance = new_attendance

    def __str__(self):
        return (f"Name: {self.name}, ID: {self.student_id}, Year: {self.year}, "
                f"CGPA: {self.cgpa:.2f}, Attendance: {self.attendance:.1f}%, "
                f"Grades: {self.grades}, Avg: {self.average_grade():.2f}")


class GradeManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        if any(s.student_id == student.student_id for s in self.students):
            print("Student ID already exists.")
        else:
            self.students.append(student)

    def find_student(self, name):
        for student in self.students:
            if student.name.lower() == name.lower():
                return student
        return None

    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def display_all_students(self):
        for student in self.students:
            print(student)


def main():
    manager = GradeManager()

    while True:
        print("\n--- Student Grade Management ---")
        print("1. Add Student")
        print("2. Add Grade")
        print("3. Update CGPA")
        print("4. Update Attendance")
        print("5. Display All Students")
        print("6. Find Student by Name")
        print("7. Find Student by ID")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            student_id = input("Enter student ID: ")
            year = input("Enter academic year (e.g., Freshman, Sophomore): ")
            try:
                cgpa = float(input("Enter CGPA: "))
                attendance = float(input("Enter attendance percentage: "))
                manager.add_student(Student(name, student_id, year, cgpa, attendance))
                print("Student added.")
            except ValueError:
                print("Invalid input for CGPA or attendance.")

        elif choice == '2':
            name = input("Enter student name to add grade: ")
            student = manager.find_student(name)
            if student:
                try:
                    grade = float(input("Enter grade: "))
                    student.add_grade(grade)
                    print("Grade added.")
                except ValueError:
                    print("Invalid grade. Please enter a number.")
            else:
                print("Student not found.")

        elif choice == '3':
            name = input("Enter student name to update CGPA: ")
            student = manager.find_student(name)
            if student:
                try:
                    new_cgpa = float(input("Enter new CGPA: "))
                    student.update_cgpa(new_cgpa)
                    print("CGPA updated.")
                except ValueError:
                    print("Invalid CGPA.")
            else:
                print("Student not found.")

        elif choice == '4':
            name = input("Enter student name to update attendance: ")
            student = manager.find_student(name)
            if student:
                try:
                    new_attendance = float(input("Enter new attendance percentage: "))
                    student.update_attendance(new_attendance)
                    print("Attendance updated.")
                except ValueError:
                    print("Invalid attendance.")
            else:
                print("Student not found.")

        elif choice == '5':
            manager.display_all_students()

        elif choice == '6':
            name = input("Enter student name to search: ")
            student = manager.find_student(name)
            if student:
                print(student)
            else:
                print("Student not found.")

        elif choice == '7':
            student_id = input("Enter student ID to search: ")
            student = manager.find_student_by_id(student_id)
            if student:
                print(student)
            else:
                print("Student not found.")

        elif choice == '8':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
