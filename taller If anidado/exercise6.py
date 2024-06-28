"""Si actualmente su capital se encuentra con saldo negativo, pedirá un préstamo bancario para que su nuevo 
saldo sea de $10,000. Si su capital tiene actualmente un saldo positivo pedirá un préstamo bancario para tener 
un nuevo saldo de $20,000, pero si su capital tiene actualmente un saldo superior a los $20 000 no pedirá 
ningún préstamo. Posteriormente repartirá su presupuesto de la siguiente manera:
 $5 000 para equipo de computo
 $2 000 para mobiliario
 y el resto la mitad será para la compra de insumos y la otra para otorgar incentivos al 
personal.
"""
capital = int(input("Enter your current capital balance: $"))

if capital < 0:
    loan_amount = 10000 - capital
    print(f"You have a negative balance. You will request a bank loan of ${loan_amount} to reach a balance of $10,000.")
    capital = 10000
elif 0 < capital <= 20000:
    loan_amount = 20000 - capital
    print(f"You will request a bank loan of ${loan_amount} to reach a balance of $20,000.")
    capital = 20000
else:
    print("Your capital balance is greater than $20,000. No loan needed.")

# Distribute budget
equipment_budget = 5000
furniture_budget = 2000
remaining_budget = capital - equipment_budget - furniture_budget
inputs_budget = remaining_budget / 2
staff_incentives = remaining_budget / 2

print("\nBudget Allocation:")
print(f"Computer Equipment: ${equipment_budget}")
print(f"Furniture: ${furniture_budget}")
print(f"Inputs: ${inputs_budget}")
print(f"Staff Incentives: ${staff_incentives}")
