from procesos.procesos_exercise1 import *



print("Welcome! in this app the students can manage their subject notes")
student_name = input("What's your name? ")
note_count = 0
total_percentage = 0
total_weighted_sum = 0

while total_percentage < 100:
    note_count += 1
    note = float(input(f'Enter the note number {note_count}: '))
    percentage = float(input(f'Enter the percentage of the note number {note_count}: '))
    total_percentage += percentage
    total_weighted_sum += promedio(note, percentage)

    if total_percentage >= 100:
        print("The percentage is already 100%")
        break
    else:
        answer = input("Do you want to add more notes? (Y/N): ").upper()
        while answer != "Y" and answer != "N":
            print("Invalid answer. Please enter Y or N.")
            answer = input("Do you want to add more notes? (Y/N): ").upper()
        if answer == "N":
            break

if total_percentage == 0:
    final_average = 0
else:
    final_average = total_weighted_sum / total_percentage

promoted_status = promoted(final_average)

print(f'The total average is {final_average:.2f}.\nThe student {student_name} is {promoted_status}.')




    
    





     
