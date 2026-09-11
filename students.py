students = []

while True:
    print("\n1. Add Student")
    print("2. Display Records")
    print("3. Search Student")
    print("4. Calculate Average")
    print("5. Display Grade")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        roll_no = input("Enter roll number: ")
        department = input("Enter department: ")
        semester = input("Enter semester: ")

        marks = []
        n = int(input("Enter number of subjects: "))

        for i in range(n):
            mark = float(input("Enter marks: "))
            marks.append(mark)

        attendance = float(input("Enter attendance: "))

        student = {
            "name": name,
            "roll_no": roll_no,
            "department": department,
            "semester": semester,
            "marks": marks,
            "attendance": attendance
        }

        students.append(student)

        print("Student added successfully.")

    elif choice == "2":
        if len(students) == 0:
            print("No records available.")
        else:
            for student in students:
                print("\nName:", student["name"])
                print("Roll Number:", student["roll_no"])
                print("Department:", student["department"])
                print("Semester:", student["semester"])
                print("Marks:", student["marks"])
                print("Attendance:", student["attendance"])

    elif choice == "3":
        roll_no = input("Enter roll number: ")
        found = False

        for student in students:
            if student["roll_no"] == roll_no:
                print("Name:", student["name"])
                print("Department:", student["department"])
                print("Semester:", student["semester"])
                print("Marks:", student["marks"])
                print("Attendance:", student["attendance"])
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "4":
        roll_no = input("Enter roll number: ")
        found = False

        for student in students:
            if student["roll_no"] == roll_no:
                average = sum(student["marks"]) / len(student["marks"])
                print("Average Marks:", round(average, 2))
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "5":
        roll_no = input("Enter roll number: ")
        found = False

        for student in students:
            if student["roll_no"] == roll_no:
                average = sum(student["marks"]) / len(student["marks"])

                if average >= 90:
                    grade = "A+"
                elif average >= 80:
                    grade = "A"
                elif average >= 70:
                    grade = "B"
                elif average >= 60:
                    grade = "C"
                elif average >= 50:
                    grade = "D"
                else:
                    grade = "F"

                print("Grade:", grade)
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "6":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")