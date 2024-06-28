"""
Un proveedor de estéreos ofrece un descuento del 10% sobre el precio sin IVA, de algún aparato si este 
cuesta $2000 o más. Además, independientemente de esto, ofrece un 5% de descuento si la marca es NOSY. 
Determinar cuánto pagara, con IVA incluido, un cliente cualquiera por la compra de su aparato.
"""
cost = int(input("How much does the stereo cost? "))
brand = input("What is the brand of the article? ").lower()

if cost >= 2000 and brand == "nosy":
    discount = 15
elif cost >= 2000:
    discount = 10
elif brand == "nosy":
    discount = 5
else:
    discount = 0

cost_with_discount = cost - (cost * discount / 100)
cost_with_vat = cost_with_discount + (cost_with_discount * 19) / 100

if discount > 0:
    print(f"You bought a {brand} brand stereo and received a {discount}% discount.") 
    print(f"The total cost with discount is {cost_with_discount}.")

else:
    print(f"You bought a {brand} brand stereo and did not receive any discount.")

print(f"The total cost with VAT included is {cost_with_vat}.")







