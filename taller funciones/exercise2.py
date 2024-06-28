from procesos.procesos_exercise2 import *   

print("Welcome to the craps game")
roll = roll_dice()
winner, throw, continue_game = calculate_first_throw(roll)
print(winner)
if continue_game:
    while True:
        next_roll = roll_dice()
        result = calculate_winner(next_roll, throw)
        if not result:
             break
else:
    print("Thanks for playing!")





   



    



   





