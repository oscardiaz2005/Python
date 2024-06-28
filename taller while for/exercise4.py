"""
El colegio Los Robles, tiene actualmente 750 estudiantes. Se espera tener un crecimiento anual de 12%. Elabore un 
algoritmo que calcule e imprima la población estudiantil que se espera tener en el año 2035
"""

# While loop
print("While loop\n")
year = 2024
students = 750
print(f'The current number of students is {students}')    

while year < 2035:
    year += 1
    students = students + (students * 12) / 100  # Increase by 12% each year
    print(f'For the year {year}, the expected number of students is {students:.0f}')  

print(f'The expected number of students for the year 2035 is {students:.0f}')
  

# For loop
print("\nFor loop\n")
year = 2024
students = 750
print(f'The current number of students is {students}')    
for i in range(year,2035,+1) :
    students = students + (students * 12) / 100  # Increase by 12% each year
    print(f'For the year {year}, the expected number of students is {students:.0f}')  

print(f'The expected number of students for the year 2035 is {students:.0f}')


