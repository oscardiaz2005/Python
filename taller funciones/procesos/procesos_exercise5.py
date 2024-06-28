def calculate_price(price1, price2, price3):
    if price1 <= price2 and price1 <= price3:
        minimum = price1
        if price2 <= price3:
            second_minimum = price2
        else:
            second_minimum = price3
    elif price2 <= price1 and price2 <= price3:
        minimum = price2
        if price1 <= price3:
            second_minimum = price1
        else:
            second_minimum = price3
    else:
        minimum = price3
        if price1 <= price2:
            second_minimum = price1
        else:
            second_minimum = price2
    
    price_to_pay = minimum + second_minimum
    
    return price_to_pay
