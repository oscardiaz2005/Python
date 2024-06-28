notes_input = input("Enter the musical notes separated by commas: ").lower()

notes_list = []

current_note = ""
for character in notes_input:
    if character == ",":
        notes_list.append(current_note)
        current_note = ""
    else:
        current_note += character

if current_note:
    notes_list.append(current_note)

unique_notes = []
note_counts = []

for note in notes_list:
    if note not in unique_notes:
        unique_notes.append(note)
        note_counts.append(1)
    else:
        index = unique_notes.index(note)
        note_counts[index] += 1

print("Musical notes:")
for note in unique_notes:
    print(note, end=" ")

print("\nFrequency of each note:")
for count in note_counts:
    print(count, end=" ")

