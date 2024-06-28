from fastapi import FastAPI
import random
from requerimientos import itsprime,calculate_salary,check_speeding,createPassword,money_back

app = FastAPI()


#EXERCISE 1
@app.get("/exercise1/{weight}/{height}")
async def Imc(weight:float,height:float):
    imc=weight/(height**2)
    return {"your IMC IS" : imc} 


#EXERCISE 2
@app.get("/exercise2/{amount}/{origin}/{destination}")
async def convert(amount: float, origin: str, destination: str):
    message = f"from {origin} to {destination} the amount is"
    result = money_back(amount, origin, destination)
    return {message: result}
    

#EXERCISE 3
@app.get("/exercise3/{distance}/{speed}")
async def time(distance:float,speed:float):
    time=distance/speed
    return {"The estimated time for your trip is=":time}


#EXERCISE 4
@app.get("/exercise4/{lenght}")
async def password(lenght:int):
    password=createPassword(lenght)
    return{"your password is= ":password}  
  

#EXERCISE 5
@app.get("/exercise5/{start}/{end}")
async def prime(start:int,end:int):
    primes=[]
    for number in range(start , end  +1):
        if itsprime(number):
            primes.append(number)
    return{"the prime numbers are" : primes}   


#EXERCISE 6
@app.get("/exercise6/{base_salary}/{overtime_hours}/{good_performance}")
async def total_salary(base_salary:int,overtime_hours:int,good_performance:str):
    cost_hour=base_salary/192
    cost_overtime_hour=cost_hour*1.25
    total_overtime_hours=overtime_hours*cost_overtime_hour
    total_salary=calculate_salary(base_salary,total_overtime_hours,good_performance)
    discount = total_salary*0.085
    total_salary_discount=total_salary-discount
    
    return{
        "your base salary is":base_salary,
    "\your money earned with overtime hours is":total_overtime_hours,
        "do you have bonification?":good_performance,
        "your salary before discounts :" :total_salary,
        "your salary after discounts :":total_salary_discount
    }


#EXERCISE 7
@app.get("/exercise7/{distance_km}/{time_minutes}/{max_speed_kmh}")
async def verify (distance_km:int,time_minutes:int,max_speed_kmh:int):
    result = check_speeding(distance_km, time_minutes, max_speed_kmh)
    return {result:""}



    






            
    

    
     


    
    
