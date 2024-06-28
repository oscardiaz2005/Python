print('WELCOME')
level = input('What is your academic level?--- secondary/professional: ').lower()

while level not in ['secondary', 'professional']:
    print('Invalid response')
    level = input('What is your academic level?--- secondary/professional: ').lower()

average = float(input('What is your average score? '))

while average < 0 or average > 10:
    print('Your average score cannot be less than 0 or greater than 10')
    average = float(input('What is your average score? '))

failed_subjects = int(input('How many subjects did you fail? '))

while failed_subjects < 0 or failed_subjects > 10:
    print('Invalid number of failed subjects')
    failed_subjects = int(input('How many subjects did you fail? '))

if average >= 9.5 and level == 'secondary':
    units = 55
    tuition_per_five_units = 180
    tuition = (units / 5) * tuition_per_five_units
    discount = tuition * 0.25
    total = tuition - discount
    print('CONGRATULATIONS! You can take 55 units and you will get a 25% discount.')
    print(f'You have to pay ${total}. This amount includes the 25% discount.')

elif 9 <= average < 9.5 and level == 'secondary':
    units = 50
    tuition_per_five_units = 180
    tuition = (units / 5) * tuition_per_five_units
    discount = tuition * 0.10
    total = tuition - discount
    print('CONGRATULATIONS! You can take 50 units and you will get a 10% discount.')
    print(f'You have to pay ${total}. This amount includes the 10% discount.')

elif 7 < average < 9 and level == 'secondary':
    units = 50
    tuition_per_five_units = 180
    tuition = (units / 5) * tuition_per_five_units
    print('CONGRATULATIONS! You can take 50 units, but you will not get any discount :(')
    print(f'You have to pay ${tuition}.')

elif average <= 7 and 0 <= failed_subjects <= 3 and level == 'secondary':
    units = 45
    tuition_per_five_units = 180
    tuition = (units / 5) * tuition_per_five_units
    print('CONGRATULATIONS! You can take 45 units, but you will not get any discount :(')
    print(f'You have to pay ${tuition}.')

elif average <= 7 and failed_subjects >= 4 and level == 'secondary':
    units = 40
    tuition_per_five_units = 180
    tuition = (units / 5) * tuition_per_five_units
    print('CONGRATULATIONS! You can take 40 units, but you will not get any discount :(')
    print(f'You have to pay ${tuition}.')

elif average >= 9.5 and level == 'professional':
    units = 55
    tuition_per_five_units = 300
    tuition = (units / 5) * tuition_per_five_units
    discount = tuition * 0.20
    total = tuition - discount
    print('CONGRATULATIONS! You can take 55 units and you will get a 20% discount.')
    print(f'You have to pay ${total}. This amount includes the 20% discount.')

elif average < 9.5 and level == 'professional':
    units = 55
    tuition_per_five_units = 300
    tuition = (units / 5) * tuition_per_five_units
    print('CONGRATULATIONS! You can take 55 units, but you will not get any discount :(')
    print(f'You have to pay ${tuition}.')
