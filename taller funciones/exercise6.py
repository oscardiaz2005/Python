from procesos.procesos_exercise6 import *
# Ask the user to enter the grades
grade1 = float(input("Enter the first grade: "))
grade2 = float(input("Enter the second grade: "))
grade3 = float(input("Enter the third grade: "))
grade4 = float(input("Enter the fourth grade: "))

# Calculate statistics
average, maximum, minimum = calculate_statistics(grade1, grade2, grade3, grade4)

# Print the results
print("Average grade:", average)
print("Maximum grade:", maximum)
print("Minimum grade:", minimum)