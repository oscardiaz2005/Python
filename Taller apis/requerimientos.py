import random

#for exercise number 2
money ={
    "cop":{"usd":0.00026, "eur":0.00024},
    "usd":{"cop":3866.15,"eur":0.92  },
    "eur":{"cop":4180.18,"usd":1.08}
}

def money_back(amount,origin,destination):
    money_find=0
    for k ,v in money.items(): 
        if k==origin:
            for a,b in v.items():
                if a==destination:
                    money_find=b
    converted_amount=money_find*amount
    return converted_amount


#for exercise number 4
def createPassword(lenght):
    chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password=""
    for i in range(lenght):
        password+=random.choice(chars)
    return password    


#for exercise number 5
def itsprime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True    


#for exercise number 6
def calculate_salary(salary,total_overtime,performance):
    if performance=="yes":
        bono=salary*0.05
        total=salary+total_overtime+bono
    else :
        total=salary+total_overtime
    return total    


#for exercise number 7
def check_speeding(distance_km, time_minutes, max_speed_kmh):
    time_hours = time_minutes / 60.0
    
    average_speed = distance_km / time_hours
    
    if average_speed > max_speed_kmh:
        return f"The driver should be fined. Average speed: {average_speed:.2f} km/h, Maximum allowed speed: {max_speed_kmh} km/h"
    else:
        return f"The driver should not be fined. Average speed: {average_speed:.2f} km/h, Maximum allowed speed: {max_speed_kmh} km/h"





    
    
