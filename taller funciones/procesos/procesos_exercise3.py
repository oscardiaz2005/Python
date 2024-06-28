def determine_even_odd(numbers):
    evens = []
    odds = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)
    return evens, odds

def first_100_perfect_numbers():
    def is_perfect(n):
        summation = 0
        for i in range(1, n):
            if n % i == 0:
                summation += i
        return summation == n
    
    perfect_numbers = []
    num = 1
    while len(perfect_numbers) < 100:
        if is_perfect(num):
            perfect_numbers.append(num)
        num += 1
    return perfect_numbers

def reverse_number(num):
    if num < 1000 or num > 9999:
        return "Invalid number. It must be a four-digit integer."
    else:
        reversed_num = 0
        for i in range(4):
            last_digit = num % 10
            num = (num - last_digit) / 10
            reversed_num = reversed_num * 10 + last_digit
        return reversed_num

