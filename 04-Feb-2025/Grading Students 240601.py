# Problem: Grading Students - https://www.hackerrank.com/challenges/grading/problem


def gradingStudents(grades):
    # Write your code here
    rounded_grades = []
    for grade in grades:
        if grade < 38:
            rounded_grades.append(grade)
        else:
            next_multiple = (grade//5 +1)*5
            if next_multiple - grade <3:
                rounded_grades.append(next_multiple)
            else:
                rounded_grades.append(grade)
    return rounded_grades