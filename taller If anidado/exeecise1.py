"""
En una fábrica de computadoras se planea ofrecer a los clientes un descuento que dependerá del número de
computadoras que compre. Si las computadoras son menos de cinco se les dará un 10% de descuento sobre el
total de la compra; si el número de computadoras es mayor o igual a cinco, pero menos de diez se le otorga
un 20% de descuento; y si son 10 o más se les da un 40% de descuento. El precio de cada computadora es de
$11,000.

"""

computer_price=11000
amount=int(input("how many computers did you buy? "))

total=amount*computer_price
if amount<5 :
    discount=total*10/100
elif amount>=5 and amount<10 :
    discount=total*10/100
elif amount>=10:
    discount=total*40 /100

total_with_discount = total-discount

print(f'your buy was {total} but as you bought {amount} computers you got a discount of  {discount}')
print(f'as a result your total is {total_with_discount}')