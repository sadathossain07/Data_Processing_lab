
marks = [ 75, 49, 73, 88, 92]
total_marks = sum(marks)
average_mark = total_marks / len(marks)
highest_mark = max(marks)
lowest_mark = min(marks)

passed_count =[grade for grade in marks if grade >= 50]

print(f"Course Marks: {marks}")
print(f"Total Marks:   {total_marks}")
print(f"Average Mark:  {average_mark:.2f}")
print(f"Highest Mark:  {highest_mark}")
print(f"Lowest Mark:   {lowest_mark}")
print(f"Passed Courses: {passed_count} out of {len(marks)}")

passed_courses = 0
fail_courses = 0
for grade in marks:
    if grade >= 50:
        passed_courses += 1
    else:
        fail_courses += 1
else:
    print(f"Total Passed Courses: {passed_courses} out of {len(marks)}")
    print(f"Total Failed Courses: {fail_courses} out of {len(marks)}")