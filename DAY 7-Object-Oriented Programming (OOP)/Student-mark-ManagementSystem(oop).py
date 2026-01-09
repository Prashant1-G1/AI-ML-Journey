class Student_manage:
    def __init__(self):
        self.student = {}

    def Add_Student(self):
        try:
            roll = int(input("Enter Roll Number: "))
        except ValueError:
            print("Please enter Roll Numebr in digit format")
            roll=int(input("Enter Roll Number: "))
        if roll in self.student:
            print("Student Already exists.")
        else:
            name = input("Enter Name: ")
            self.student[roll] = {"Name": name, "Marks": {}}
            print("Student Added Successfully.")

    def Remove_Student(self):
        roll = int(input("Enter Roll Number: "))
        if roll in self.student:
            del self.student[roll]
            print("Student Removed Successfully")
        else:
            print("Student Not Available")

    def Manage_Marks(self):
        roll = int(input("Enter Roll Number: "))
        if roll not in self.student:
            print("Student not found")
        else:
            subject = input("Enter Subject Name: ")
            marks = int(input("Enter subject Marks: "))
            if marks < 0 or marks > 100:
                print("Invalid Marks.")
            else:
                self.student[roll]["Marks"][subject] = marks
                print("Marks Added Successfully.")

    def remove_subject(self):
        roll = int(input("Enter Roll Number: "))
        if roll not in self.student:
            print("Student Not Found.")
        else:
            subject = input("Enter Subject Name: ")
            if subject in self.student[roll]["Marks"]:
                del self.student[roll]["Marks"][subject]
                print("Subject Removed Successfully.")
            else:
                print("Subject not found.")

    def view_Student(self):
        roll = int(input("Enter Roll Number: "))
        if roll not in self.student:
            print("Student Not Found.")
        else:
            total = 0
            print()
            print(f"Roll Number: {roll}")
            print(f"Name: {self.student[roll]['Name']}")
            print("\nMarks Obtained:")

            if not self.student[roll]["Marks"]:
                print("No marks available.")
                return

            for subject, marks in self.student[roll]["Marks"].items():
                print(f"{subject}: {marks}")
                total += marks

            average = total // len(self.student[roll]["Marks"])
            print(f"Total = {total}")
            print(f"Average = {average}")

    def view_All_student(self):
        if self.student:
            for roll, data in self.student.items():
                print(f"Roll Number: {roll}")
                print(f"Name: {data['Name']}")
                print("-" * 20)
        else:
            print("No Students")

    def menu(self):
        while True:
            print("\n******** Student Management Menu ********")
            print("1. Add Student")
            print("2. Remove Student")
            print("3. Manage Marks")
            print("4. Remove Subject")
            print("5. View Student")
            print("6. View All Students")
            print("7. Exit")

            select = int(input("Select From (1-7): "))

            if select == 1:
                self.Add_Student()
            elif select == 2:
                self.Remove_Student()
            elif select == 3:
                self.Manage_Marks()
            elif select == 4:
                self.remove_subject()
            elif select == 5:
                self.view_Student()
            elif select == 6:
                self.view_All_student()
            elif select == 7:
                print("Exit successfully")
                break
            else:
                print("Invalid Selection.")


sm = Student_manage()
sm.menu()

            