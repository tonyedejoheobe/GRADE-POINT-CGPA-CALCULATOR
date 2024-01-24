def calculate_grade_points(grade):
    grade_points = {'A': 5.0, 'B': 4.0, 'C': 3.0, 'D': 2.0, 'E': 1.0, 'F': 0.0}
    return grade_points.get(grade.upper(), 0.0)

def calculate_sgpa():
    total_credit_hours = 0
    total_grade_points = 0

    num_courses = int(input("Enter the number of courses: "))

    for _ in range(num_courses):
        course_name = input("Enter the course name: ")
        credit_hours = float(input("Enter the credit unit for {}: ".format(course_name)))
        grade_obtained = input("Enter the grade obtained (A to F) for {}: ".format(course_name))

        grade_points = calculate_grade_points(grade_obtained)
        total_credit_hours += credit_hours
        total_grade_points += grade_points * credit_hours

    if total_credit_hours == 0:
        return 0.0

    sgpa = total_grade_points / total_credit_hours
    return sgpa

# Example usage:
sgpa_result = calculate_sgpa()

if sgpa_result:
    print("Your SGPA for the semester is: {:.2f}".format(sgpa_result))
else:
    print("Error: Total credit hours cannot be zero.")