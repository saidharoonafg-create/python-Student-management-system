import json

# File to store data
FILE_NAME = "students.json"

# Load data from file
def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []

# Save data to file
def save_data(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

# Add student
def add_student(students):
    print("\n--- Add Student ---")
    student = {}

    student["id"] = input("Enter ID: ")
    student["name"] = input("Enter Name: ")
    student["age"] = int(input("Enter Age: "))
    student["course"] = input("Enter Course: ")

    marks = []
    for i in range(3):
        mark = float(input(f"Enter marks for subject {i+1}: "))
        marks.append(mark)

    student["marks"] = marks
    students.append(student)

    save_data(students)
    print("Student added successfully!")

# View students
def view_students(students):
    print("\n--- All Students ---")
    if not students:
        print("No records found.")
        return

    for s in students:
        print(s)

# Search student
def search_student(students):
    sid = input("Enter Student ID to search: ")

    for s in students:
        if s["id"] == sid:
            print("Student Found:", s)
            return

    print("Student not found.")

# Update student
def update_student(students):
    sid = input("Enter Student ID to update: ")

    for s in students:
        if s["id"] == sid:
            s["name"] = input("Enter new name: ")
            s["age"] = int(input("Enter new age: "))
            s["course"] = input("Enter new course: ")

            marks = []
            for i in range(3):
                mark = float(input(f"Enter new marks for subject {i+1}: "))
                marks.append(mark)

            s["marks"] = marks

            save_data(students)
            print("Student updated!")
            return

    print("Student not found.")

# Delete student
def delete_student(students):
    sid = input("Enter Student ID to delete: ")

    for s in students:
        if s["id"] == sid:
            students.remove(s)
            save_data(students)
            print("Student deleted!")
            return

    print("Student not found.")

# Statistics
def statistics(students):
    print("\n--- Class Statistics ---")

    if not students:
        print("No data available.")
        return

    all_marks = []
    top_student = None
    highest_avg = 0

    for s in students:
        avg = sum(s["marks"]) / len(s["marks"])
        all_marks.extend(s["marks"])

        if avg > highest_avg:
            highest_avg = avg
            top_student = s

    print("Average Marks:", sum(all_marks)/len(all_marks))
    print("Highest Marks:", max(all_marks))
    print("Lowest Marks:", min(all_marks))
    print("Top Student:", top_student["name"], "with avg:", highest_avg)

# Menu
def menu():
    students = load_data()

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Statistics")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            statistics(students)
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

# Run program
menu()