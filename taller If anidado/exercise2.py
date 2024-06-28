"""En una llantera se ha establecido una promoción de las llantas marca Ponchadas, dicha promoción consiste en
lo siguiente: Si se compran menos de cinco llantas el precio es de $300 cada una, de $250 si se compran de
cinco a 10 y de $200 si se compran más de 10. Obtener la cantidad de dinero que una persona tiene que pagar
por cada una de las llantas que compra y la que tiene que pagar por el total de la compra.
"""
amount=int(input("how many tires did you buy? "))
if amount<5 :
    tire_price=300
elif amount>=5 and amount<=10:
    tire_price=250
elif amount>10 :
    tire_price=200

total=amount*tire_price

print(f' you bought {amount} tires , the cost of each of them was {tire_price} your total is {total}')







