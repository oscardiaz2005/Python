def calculate_statistics(grade1, grade2, grade3, grade4):
    average_grade = (grade1 + grade2 + grade3 + grade4) / 4
    
    max_grade = grade1
    if grade2 > max_grade:
        max_grade = grade2
    if grade3 > max_grade:
        max_grade = grade3
    if grade4 > max_grade:
        max_grade = grade4
    
    min_grade = grade1
    if grade2 < min_grade:
        min_grade = grade2
    if grade3 < min_grade:
        min_grade = grade3
    if grade4 < min_grade:
        min_grade = grade4
    
    return average_grade, max_grade, min_grade