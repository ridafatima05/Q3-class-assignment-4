#STUDENT GRADING MANAGEMENT SYSTEM:

# Student list to store student dictionaries
students = [
    {
        "name": "Shasmeen",
        "id": 101,
        "grades": {
            "Math": 85,
            "English": 78,
            "Science": 90
        }
    },
    {
        "name": "Ifza",
        "id": 102,
        "grades": {
            "Math": 95,
            "English": 88,
            "Science": 92
        }
    },
    {
        "name": "Aiman",
        "id": 103,
        "grades": {
            "Math": 70,
            "English": 65,
            "Science": 75
        }
    }
]

# Display all students with their grades
print("📚 All Students and Their Grades:")
for student in students:
    print(f"\nName: {student['name']}, ID: {student['id']}")
    for course, grade in student['grades'].items():
        print(f"  {course}: {grade}")

# Calculate and display average grade for each student
print("\n📊 Average Grade for Each Student:")
for student in students:
    grades = student["grades"].values()
    avg = sum(grades) / len(grades)
    print(f"{student['name']} - Average Grade: {avg:.2f}")

# Find and display student with highest average grade
highest_avg = 0
top_student = None
for student in students:
    avg = sum(student["grades"].values()) / len(student["grades"])
    if avg > highest_avg:
        highest_avg = avg
        top_student = student
print(f"\n🏆 Top Student: {top_student['name']} with Average Grade {highest_avg:.2f}")

# List students with average grade above 80
print("\n🎯 Students with Average Grade Above 80:")
for student in students:
    avg = sum(student["grades"].values()) / len(student["grades"])
    if avg > 80:
        print(f"{student['name']} - {avg:.2f}")

# Calculate and display average grade for a specific course
specific_course = "Math"
total = 0
count = 0
for student in students:
    if specific_course in student["grades"]:
        total += student["grades"][specific_course]
        count += 1

if count > 0:
    course_avg = total / count
    print(f"\n📐 Average Grade in {specific_course}: {course_avg:.2f}")
else:
    print(f"No data for the course: {specific_course}")

# Add a new student to the system
new_student = {
    "name": "Rida",
    "id": 104,
    "grades": {
        "Math": 100,
        "English": 91,
        "Science": 85
    }
}
students.append(new_student)
print(f"\n✅ New Student Added: {new_student['name']} (ID: {new_student['id']})")
