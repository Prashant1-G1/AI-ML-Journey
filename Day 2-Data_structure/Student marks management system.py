# Student Marks Management System

students = {}

def add_student():
    roll = int(input("Enter roll number: "))
    if roll in students:
        print("Student already exists.")
        return
    name = input("Enter student name: ")
    students[roll] = {
        "name": name,
        "marks": {}
    }
    print("Student added successfully.")

def add_or_update_marks():
    roll = int(input("Enter roll number: "))
    if roll not in students:
        print("Student not found.")
        return

    subject = input("Enter subject name: ")
    marks = int(input("Enter marks (0–100): "))

    if marks < 0 or marks > 100:
        print("Invalid marks.")
        return

    students[roll]["marks"][subject] = marks
    print("Marks updated successfully.")

def view_student():
    roll = int(input("Enter roll number: "))
    if roll not in students:
        print("Student not found.")
        return

    student = students[roll]
    print("\nName:", student["name"])
    print("Marks:")

    total = 0
    count = 0

    for subject, marks in student["marks"].items():
        print(f"  {subject}: {marks}")
        total += marks
        count += 1

    if count > 0:
        average = total / count
        print("Total:", total)
        print("Average:", average)
        print("Result:", "Pass" if average >= 40 else "Fail")
    else:
        print("No marks available.")

def view_all_students():
    if not students:
        print("No student records found.")
        return

    for roll, data in students.items():
        print(f"\nRoll: {roll}")
        print("Name:", data["name"])
        for subject , mark in students[roll]["marks"].items():
            print(f"{subject}: {mark}")

def main_menu():
    while True:
        print("\n--- Student Marks Management System ---")
        print("1. Add Student")
        print("2. Add / Update Marks")
        print("3. View Student Details")
        print("4. View All Students")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            add_or_update_marks()
        elif choice == "3":
            view_student()
        elif choice == "4":
            view_all_students()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

# Run the program
main_menu()

    






