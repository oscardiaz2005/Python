"""
Una empresa vende hojas y hielo seco con las condiciones siguientes: 
• Si el cliente es tipo 1 se le descuenta el 5%. 
• Si el cliente es tipo 2 se le descuenta el 8%. 
• Si el cliente es tipo 3 se le descuenta el 12%. 
• Si el cliente es tipo 4 se le descuenta el 15%. 
Cuando un cliente realiza una compra generan los datos siguientes 
• Nombre del cliente 
• Tipo de cliente (1,2,3,4) 
• cantidad de hojas compradas 
• Precio por hoja 
Elaborar un algoritmo que permita procesar varios clientes e imprima el reporte. 
"""

# While loop
print("While loop\n")
price_sheet = 500
amount = int(input("how many customers are going to buy? "))
customer = 1
while customer <= amount:
    name = input(f'\nhi customer {customer} what is your name ? ')
    type = int(input("which is your type? 1/2/3/4 "))
    while type > 4 or type < 1:
        print("invalid type")
        type = int(input("which is your type? 1/2/3/4 "))
    if type == 1:
        discount = 5
    elif type == 2:
        discount = 8
    elif type == 3:
        discount = 12
    elif type == 4:
        discount = 15
    print(f'your discount is {discount}%')
    amount_sheet = int(input("how many sheets of paper are you gonna buy? "))
    total = amount_sheet * price_sheet
    total_discounted = total - (total * discount) / 100

    print("purchase summary\n")
    print(name)
    print(f'Type = {type}')
    print(f'number of sheets purchased = {amount_sheet}')
    print(f'cost per sheet = {price_sheet}')
    print(f'total = {total}')
    print(f'total with discount = {total_discounted}')

    customer += 1



# For loop
print("\nFor loop\n")
price_sheet = 500
amount = int(input("how many customers are going to buy? "))
for i in range(amount):
    name = input(f'\nhi customer {i+1} what is your name ? ')
    type = int(input("which is your type? 1/2/3/4 "))
    while type > 4 or type < 1:
        print("invalid type")
        type = int(input("which is your type? 1/2/3/4 "))
    if type == 1:
        discount = 5
    elif type == 2:
        discount = 8
    elif type == 3:
        discount = 12
    elif type == 4:
        discount = 15
    print(f'your discount is {discount}%')
    amount_sheet = int(input("how many sheets of paper are you gonna buy? "))
    total = amount_sheet * price_sheet
    total_discounted = total - (total * discount) / 100

    print("purchase summary\n")
    print(name)
    print(f'Type = {type}')
    print(f'number of sheets purchased = {amount_sheet}')
    print(f'cost per sheet = {price_sheet}')
    print(f'total = {total}')
    print(f'total with discount = {total_discounted}')

