import csv

def enter_marks():
    students = {}
    n = int(input("Enter number of students: "))
    for i in range(n):
        name = input(f"Enter name of student {i+1}: ")
        marks = float(input(f"Enter marks for {name}: "))
        students[name] = marks
    return students


def read_from_csv():
    students = {}
    filename = input("Enter CSV file name (with .csv extension): ")
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            next(reader, None)
            for row in reader:
                if len(row) >= 2:
                    students[row[0]] = float(row[1])
    except FileNotFoundError:
        print("File not found. Please check the file name.")
    return students


def analyze_marks(students):
    marks = list(students.values())
    if not marks:
        print("No student data available.")
        return
    top_score = max(marks)
    avg_score = sum(marks) / len(marks)
    pass_count = len([m for m in marks if m >= 40])
    fail_count = len(marks) - pass_count

    print("\n--- Class Analysis ---")
    print(f"Top Score: {top_score}")
    print(f"Average Score: {avg_score:.2f}")
    print(f"Pass Count: {pass_count}")
    print(f"Fail Count: {fail_count}")


def assign_grades(students):
    grades = {}
    for name, marks in students.items():
        if marks >= 90:
            grade = "A"
        elif marks >= 80:
            grade = "B"
        elif marks >= 70:
            grade = "C"
        elif marks >= 60:
            grade = "D"
        else:
            grade = "F"
        grades[name] = grade
    return grades


def pass_fail_summary(students):
    passed = [name for name, marks in students.items() if marks >= 40]
    failed = [name for name, marks in students.items() if marks < 40]

    print("\n--- Pass/Fail Summary ---")
    print("Passed Students:", ", ".join(passed) if passed else "None")
    print("Failed Students:", ", ".join(failed) if failed else "None")


def display_results(students, grades):
    print("\nName\t\tMarks\tGrade")
    print("-" * 30)
    for name, marks in students.items():
        print(f"{name:<10}\t{marks:<6}\t{grades[name]}")


def export_results(students, grades):
    filename = "results.csv"
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Marks", "Grade"])
        for name, marks in students.items():
            writer.writerow([name, marks, grades[name]])
    print(f"\nResults exported successfully to {filename}")


def main():
    while True:
        print("\n--- Student Marks Analyzer ---")
        print("1. Enter student marks manually")
        print("2. Read marks from a CSV file")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            students = enter_marks()
        elif choice == "2":
            students = read_from_csv()
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
            continue

        analyze_marks(students)
        grades = assign_grades(students)
        pass_fail_summary(students)
        display_results(students, grades)

        export_choice = input("\nDo you want to export results to CSV? (y/n): ").lower()
        if export_choice == "y":
            export_results(students, grades)

        again = input("\nDo you want to analyze again? (y/n): ").lower()
        if again != "y":
            print("Thank you for using the Student Marks Analyzer!")
            break


if __name__ == "__main__":
    main()