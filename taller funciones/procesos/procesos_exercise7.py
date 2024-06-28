def max_product_of_two(num1, num2, num3, num4):
    products = [num1*num2, num1*num3, num1*num4, num2*num3, num2*num4, num3*num4]
    max_product = products[0]
    for product in products[1:]:
        if product > max_product:
            max_product = product
    return max_product