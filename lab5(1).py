
students = [
    ("Alice", 2),
    ("Bob", 1),
    ("Charlie", 3),
    ("David", 1),
    ("Eve", 2)
]

students.sort(key=lambda student: student[1])

for student in students:
    print(student[0], "in class", student[1])

grades = {
    "Alice": {"math": 85, "history": 90, "programming": 95},
    "Bob": {"math": 80, "history": 85, "programming": 90},
    "Charlie": {"math": 90, "history": 95, "programming": 80},
    "David": {"math": 75, "history": 80, "programming": 85},
    "Eve": {"math": 95, "history": 90, "programming": 90}
}

def lookup_grades(name):
    if name in grades:
        return grades[name]
    else:
        return None

name = input("Enter a student's name: ")

grades = lookup_grades(name)
if grades is not None:
    print("Grades for", name)
    for subject, grade in grades.items():
        print(subject, ":", grade)
else:
    print("Student not found")
