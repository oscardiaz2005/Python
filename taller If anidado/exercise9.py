"""Realice un ejercicio donde al insertar las notas de cuatro materias de un estudiante, 
le muestre si según la nota numérica el estudiante tiene excelente sobresaliente 
aceptable insuficiente y deficiente. El rango es el siguiente 0 a 1 D, 1,1 a 2,9 I, 
3 a 3,8 A, de 3,9 a 4,6 S y de 4,7 a 5 E debe calcularlo para 4 periodos del año 
y hacer un promedio de todas las notas si el promedio es igual o mayor a 3,5 debe 
salir un mensaje que diga el estudiante es Promovido al siguiente grado debe 
aparecer al grado al que es promovido. Si el estudiante está cursando 11 debe
aparecer el estudiante puede graduarse de lo contrario debe aparecer un letrero 
que diga el estudiante NO ES PROMOVID"""
# Ask the user for the student's grade number

grade = int(input("Enter the student's grade number: "))

period = 1
total_average = 0

while period <= 4:
    print(f"For period {period}:")
    subject = 1
    total_period_grade = 0
    
    while subject <= 4:
        note = float(input(f"Enter the grade for subject {subject}: "))
        total_period_grade += note

        if note >= 4.7:
            classification = 'E'
        elif note>= 3.9:
            classification = 'S'
        elif note >= 3.0:
            classification = 'A'
        elif note >= 1.1:
            classification = 'I'
        else:
            classification = 'D'
        
        print(f"Subject {subject} classification: {classification}")
        
        subject += 1
    
    period_average = total_period_grade / 4
    total_average += period_average
    print(f"Average grade for period {period}: {period_average}")
    
    period += 1

total_average /= 4
print(f"Total average grade: {total_average}")

if total_average >= 4.7:
    total_classification = 'E'
elif total_average >= 3.9:
    total_classification = 'S'
elif total_average >= 3.0:
    total_classification = 'A'
elif total_average >= 1.1:
    total_classification = 'I'
else:
    total_classification = 'D'

if total_average >= 3.5:
    if grade == 11:
        print("The student can graduate.")
    else:
        print("The student is promoted to the next grade:", grade + 1)
else:
    print("The student is NOT PROMOTED.")
