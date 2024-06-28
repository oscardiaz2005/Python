def is_divisor(number, divisor):
    if divisor == 0:
        return False
    
    if number % divisor == 0:
        return True
    else:
        return False
