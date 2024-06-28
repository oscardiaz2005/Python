"""
pedir x canidad de productos =nombre y valor
se debe poder realizar una venta del producto donde el cliente pide un producto por el nombre cantidad de ese producto 
"""
def calculate_cost (amount, cost):
    total=amount*cost
    return total

products=[]
costs=[]
amount_products=int(input("how many pruducts do you want to add? "))
for i in range(amount_products):
    product=input(f'enter the product number {i+1} ')
    cost= int(input(f'enter the cost of the  product  number {i+1} '))
    products.append(product)
    costs.append(cost)

final_cost=0

while True :
    print("PRODUCTS")
    for i in range(len(products)):
        print (i+1 , products[i])
    buy_product=int(input("enter the product's code you want to buy (enter 0 to end) "))
    if buy_product==0:
        print("thanku for purchasing")
        break
    amount_buy=int(input("enter the amount you want to buy "))
    principal_cost=calculate_cost(amount_buy ,costs[buy_product-1])
    print("purchase made , the total of this purchase was ",principal_cost)
    final_cost+=principal_cost

print(f'your total is  {final_cost}')    