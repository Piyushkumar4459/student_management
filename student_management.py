
import json
import os

FILE_NAME = "students.json"


def load_students():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Warning: Could not read student records.")
    return []


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def add_student(students):
    roll = input("Enter roll number: ").strip()

    if any(s["roll"] == roll for s in students):
        print("A student with this roll number already exists.")
        return

    name = input("Enter student name: ").strip()

    try:
        marks = float(input("Enter marks (0-100): "))
        if not name or not roll or not 0 <= marks <= 100:
            print("Invalid name, roll number, or marks.")
            return
    except ValueError:
        print("Marks must be a valid number.")
        return

    students.append({
        "roll": roll,
        "name": name,
        "marks": marks
    })

    save_students(students)
    print("Student added successfully!")


def view_students(students):
    if not students:
        print("No student records found.")
        return

    print("\n--- Student Records ---")
    for student in students:
        print(
            f"Roll: {student['roll']} | "
            f"Name: {student['name']} | "
            f"Marks: {student['marks']}"
        )


def search_student(students):
    roll = input("Enter roll number to search: ").strip()

    for student in students:
        if student["roll"] == roll:
            print("\nStudent found!")
            print("Roll Number:", student["roll"])
            print("Name:", student["name"])
            print("Marks:", student["marks"])
            return

    print("Student not found.")


def delete_student(students):
    roll = input("Enter roll number to delete: ").strip()

    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            save_students(students)
            print("Student deleted successfully!")
            return

    print("Student not found.")


def main():
    students = load_students()

    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
