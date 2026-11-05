
import json
import os
from datetime import datetime

FILE_NAME = "students.json"


class Student:
    def __init__(self, student_id, name, age, course):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.marks = {}
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def add_marks(self, subject, marks):
        if not 0 <= marks <= 100:
            raise ValueError("Marks must be between 0 and 100.")
        self.marks[subject] = marks

    def calculate_average(self):
        if not self.marks:
            return 0
        return sum(self.marks.values()) / len(self.marks)

    def calculate_grade(self):
        if not self.marks:
            return "N/A"

        average = self.calculate_average()

        if average >= 90:
            return "A+"
        elif average >= 80:
            return "A"
        elif average >= 70:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 50:
            return "D"
        else:
            return "F"

    def display_details(self):
        print("\n" + "=" * 45)
        print("STUDENT DETAILS")
        print("=" * 45)
        print(f"Student ID : {self.student_id}")
        print(f"Name       : {self.name}")
        print(f"Age        : {self.age}")
        print(f"Course     : {self.course}")
        print(f"Created At : {self.created_at}")

        print("\nSubject Marks:")
        if self.marks:
            for subject, mark in self.marks.items():
                print(f"  {subject}: {mark}")
        else:
            print("  No marks available.")

        print(f"\nAverage: {self.calculate_average():.2f}")
        print(f"Grade  : {self.calculate_grade()}")
        print("=" * 45)

    def to_dictionary(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "course": self.course,
            "marks": self.marks,
            "created_at": self.created_at
        }


class StudentManagementSystem:
    def __init__(self):
        self.students = {}
        self.load_data()

    def load_data(self):
        if not os.path.exists(FILE_NAME):
            return

        try:
            with open(FILE_NAME, "r", encoding="utf-8") as file:
                data = json.load(file)

            for item in data:
                student = Student(
                    item["student_id"],
                    item["name"],
                    item["age"],
                    item["course"]
                )

                student.marks = item.get("marks", {})
                student.created_at = item.get(
                    "created_at", student.created_at
                )

                self.students[student.student_id] = student

            print("Student records loaded successfully.")

        except (OSError, ValueError, KeyError, TypeError) as error:
            print(f"Error loading data: {error}")

    def save_data(self):
        data = [
            student.to_dictionary()
            for student in self.students.values()
        ]

        try:
            with open(FILE_NAME, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)

            print("Data saved successfully.")

        except OSError as error:
            print(f"Error saving data: {error}")

    def add_student(self):
        print("\n--- Add New Student ---")

        student_id = input("Enter Student ID: ").strip()

        if not student_id:
            print("Student ID cannot be empty.")
            return

        if student_id in self.students:
            print("Student ID already exists.")
            return

        name = input("Enter Student Name: ").strip()

        if not name:
            print("Student name cannot be empty.")
            return

        try:
            age = int(input("Enter Age: "))

            if age <= 0:
                print("Age must be positive.")
                return

        except ValueError:
            print("Please enter a valid age.")
            return

        course = input("Enter Course: ").strip()

        student = Student(student_id, name, age, course)
        self.students[student_id] = student

        self.save_data()
        print("Student added successfully!")

    def view_all_students(self):
        if not self.students:
            print("\nNo student records found.")
            return

        print("\n" + "-" * 75)
        print(f"{'ID':<12}{'Name':<22}{'Course':<20}{'Grade':<10}")
        print("-" * 75)

        for student in self.students.values():
            print(
                f"{student.student_id:<12}"
                f"{student.name:<22}"
                f"{student.course:<20}"
                f"{student.calculate_grade():<10}"
            )

        print("-" * 75)

    def search_student(self):
        keyword = input("\nEnter ID or Name: ").strip().lower()

        results = []

        for student in self.students.values():
            if (
                keyword in student.student_id.lower()
                or keyword in student.name.lower()
            ):
                results.append(student)

        if not results:
            print("No matching students found.")
            return

        for student in results:
            student.display_details()

    def update_student(self):
        student_id = input("\nEnter Student ID: ").strip()

        if student_id not in self.students:
            print("Student not found.")
            return

        student = self.students[student_id]

        print("\nLeave blank to keep existing information.")

        name = input(f"Name ({student.name}): ").strip()
        age = input(f"Age ({student.age}): ").strip()
        course = input(f"Course ({student.course}): ").strip()

        if age:
            try:
                new_age = int(age)
                if new_age <= 0:
                    print("Age must be positive.")
                    return
                student.age = new_age
            except ValueError:
                print("Invalid age.")
                return

        if name:
            student.name = name

        if course:
            student.course = course

        self.save_data()
        print("Student updated successfully!")

    def delete_student(self):
        student_id = input("\nEnter Student ID: ").strip()

        if student_id not in self.students:
            print("Student not found.")
            return

        confirmation = input(
            "Are you sure you want to delete this student? (yes/no): "
        ).lower()

        if confirmation == "yes":
            del self.students[student_id]
            self.save_data()
            print("Student deleted successfully.")
        else:
            print("Deletion cancelled.")

    def add_student_marks(self):
        student_id = input("\nEnter Student ID: ").strip()

        if student_id not in self.students:
            print("Student not found.")
            return

        student = self.students[student_id]

        while True:
            subject = input("\nEnter Subject Name (or 'done'): ").strip()

            if subject.lower() == "done":
                break

            if not subject:
                print("Subject cannot be empty.")
                continue

            try:
                marks = float(input("Enter Marks (0-100): "))
                student.add_marks(subject, marks)
                print("Marks added successfully.")

            except ValueError as error:
                print(f"Invalid marks: {error}")

        self.save_data()

    def show_top_students(self):
        students_with_marks = [
            student
            for student in self.students.values()
            if student.marks
        ]

        if not students_with_marks:
            print("No student marks available.")
            return

        ranked_students = sorted(
            students_with_marks,
            key=lambda student: student.calculate_average(),
            reverse=True
        )

        print("\n--- Top Performing Students ---")

        for rank, student in enumerate(ranked_students[:5], start=1):
            print(
                f"{rank}. {student.name} - "
                f"{student.calculate_average():.2f}% "
                f"({student.calculate_grade()})"
            )

    def calculate_statistics(self):
        if not self.students:
            print("No student data available.")
            return

        total_students = len(self.students)

        students_with_marks = [
            student
            for student in self.students.values()
            if student.marks
        ]

        print("\n" + "=" * 45)
        print("STUDENT STATISTICS")
        print("=" * 45)

        print(f"Total Students: {total_students}")
        print(f"Students with Marks: {len(students_with_marks)}")

        if students_with_marks:
            averages = [
                student.calculate_average()
                for student in students_with_marks
            ]

            overall_average = sum(averages) / len(averages)

            highest = max(
                students_with_marks,
                key=lambda student: student.calculate_average()
            )

            lowest = min(
                students_with_marks,
                key=lambda student: student.calculate_average()
            )

            print(f"Overall Average: {overall_average:.2f}%")
            print(f"Highest Performer: {highest.name}")
            print(f"Lowest Performer : {lowest.name}")

            passed = sum(
                1 for student in students_with_marks
                if student.calculate_average() >= 50
            )

            failed = len(students_with_marks) - passed

            print(f"Passed: {passed}")
            print(f"Failed: {failed}")

            pass_percentage = (
                passed / len(students_with_marks)
            ) * 100

            print(f"Pass Percentage: {pass_percentage:.2f}%")

        print("=" * 45)

    def filter_by_course(self):
        course = input("\nEnter Course Name: ").strip().lower()

        matching_students = [
            student
            for student in self.students.values()
            if student.course.lower() == course
        ]

        if not matching_students:
            print("No students found for this course.")
            return

        print(f"\nStudents enrolled in {course.title()}:")

        for student in matching_students:
            print(f"- {student.name} ({student.student_id})")

    def export_report(self):
        report_name = "student_report.txt"

        try:
            with open(report_name, "w", encoding="utf-8") as file:
                file.write("STUDENT MANAGEMENT REPORT\n")
                file.write("=" * 50 + "\n")
                file.write(
                    f"Generated: {datetime.now()}\n\n"
                )

                for student in self.students.values():
                    file.write(
                        f"ID: {student.student_id}\n"
                    )
                    file.write(
                        f"Name: {student.name}\n"
                    )
                    file.write(
                        f"Course: {student.course}\n"
                    )
                    file.write(
                        f"Average: {student.calculate_average():.2f}\n"
                    )
                    file.write(
                        f"Grade: {student.calculate_grade()}\n"
                    )
                    file.write("-" * 50 + "\n")

            print(f"Report exported to {report_name}")

        except OSError as error:
            print(f"Export failed: {error}")


def display_menu():
    print("\n" + "=" * 50)
    print("        STUDENT MANAGEMENT SYSTEM")
    print("=" * 50)

    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Add Student Marks")
    print("7. Show Top Students")
    print("8. View Statistics")
    print("9. Filter Students by Course")
    print("10. Export Student Report")
    print("11. Exit")

    print("=" * 50)


def main():
    system = StudentManagementSystem()

    actions = {
        "1": system.add_student,
        "2": system.view_all_students,
        "3": system.search_student,
        "4": system.update_student,
        "5": system.delete_student,
        "6": system.add_student_marks,
        "7": system.show_top_students,
        "8": system.calculate_statistics,
        "9": system.filter_by_course,
        "10": system.export_report
    }

    while True:
        display_menu()

        choice = input("Enter your choice (1-11): ").strip()

        if choice == "11":
            system.save_data()
            print("\nThank you for using Student Management System!")
            print("Goodbye!")
            break

        action = actions.get(choice)

        if action:
            action()
        else:
            print("Invalid choice. Please select 1-11.")


if __name__ == "__main__":
    main()
