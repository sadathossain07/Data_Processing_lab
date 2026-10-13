
students = [
    {"name": "Rahim", "department": "CSE", "marks": 85, "attendance": 92},
    {"name": "Karim", "department": "CSE", "marks": 48, "attendance": 76},
    {"name": "Sara", "department": "DS", "marks": 91, "attendance": 95},
    {"name": "Nadia", "department": "DS", "marks": 67, "attendance": 84},
    {"name": "Hasan", "department": "CSE", "marks": 73, "attendance": 78}
]

def calculate_average_marks(student_list):
    total = 0
    for s in student_list:
        total += s["marks"]
    return total / len(student_list)

def find_top_student(student_list):
    top_student = student_list[0]
    for s in student_list:
        if s["marks"] > top_student["marks"]:
            top_student = s
    return top_student

def count_low_attendance(student_list):
    count = 0
    for s in student_list:
        if s["attendance"] < 80:
            count += 1
    return count


avg_marks = calculate_average_marks(students)
top_student = find_top_student(students)
low_attendance_count = count_low_attendance(students)

print("=" * 35)
print("     STUDENT DATA SUMMARY")
print("=" * 35)
print(f"Class Average Marks:        {avg_marks:.2f}")
print(f"Top Performer:              {top_student['name']} ({top_student['marks']} marks)")
print(f"Students Attendance < 80%:  {low_attendance_count}")
print("=" * 35)