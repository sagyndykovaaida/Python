students = []

num_students = int(input("Enter the number of students: "))
for i in range(num_students):
    name = input("Enter the student's name: ")
    cls = int(input("Enter the student's class number: "))
    students.append((cls, name))  
students.sort()

print("List of surnames and classes:")
for student in students:
    print(student[1], student[0])
