<<<<<<< HEAD
def calculate_grade(marks):
    # Calculate average
    avg = sum(marks) / len(marks)
    
    # Determine grade
    if avg >= 80:
        grade = "A"
    elif avg >= 70:
        grade = "B"
    elif avg >= 60:
        grade = "C"
    elif avg >= 50:
        grade = "D"
    else:
        grade = "F"
        
    return avg, grade

course_marks = [82, 75, 88, 69, 91]
avg, result_grade = calculate_grade(course_marks)

print(f"Marks: {course_marks}")
print(f"Average: {avg:.2f}")
=======
def calculate_grade(marks):
    # Calculate average
    avg = sum(marks) / len(marks)
    
    # Determine grade
    if avg >= 80:
        grade = "A"
    elif avg >= 70:
        grade = "B"
    elif avg >= 60:
        grade = "C"
    elif avg >= 50:
        grade = "D"
    else:
        grade = "F"
        
    return avg, grade

course_marks = [82, 75, 88, 69, 91]
avg, result_grade = calculate_grade(course_marks)

print(f"Marks: {course_marks}")
print(f"Average: {avg:.2f}")
>>>>>>> e9f3b641592de2382b358d3f06bfd1fc013d08ba
print(f"Final Grade: {result_grade}")