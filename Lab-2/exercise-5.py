
student = {
    "Name": "Rahim",
    "ID": "011231001",
    "Department": "Data Science",
    "CGPA": 3.45
}

print("Student Information:")
for key, value in student.items():
    print(f"{key}: {value}")


print("\nAcademic Standing:")
if student["CGPA"] >= 2.50:
    print("Status: Good Standing")
else:
    print("Status: Academic Warning")
