notes=[]
minor_note=11
mayor_note=-1
for i in range(5):
    note=float (input(f'please enter the note number {i+1} '))
    while note <0 or note >10 :
        print("invalid note")
        note=float (input(f'please enter the note number {i+1} '))
    if note>mayor_note:
        mayor_note=note
    if note<minor_note:
        minor_note=note          
  
    notes.append(note)

print(f'the notes are  {notes} ')
print( f'the middle note is {notes[2]}')
print( f'the mayor note is {mayor_note}')
print( f'the minor note is {minor_note}')
