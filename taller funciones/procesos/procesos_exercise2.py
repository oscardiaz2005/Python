import random

def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)


def calculate_first_throw(roll):
    if roll == 7 or roll == 11:
        continue_game = False
        return "You rolled a natural! You won the game!", roll, continue_game
    elif roll == 2 or roll == 3 or roll == 12:
        continue_game = False
        return "Craps! You lost the game.", roll, continue_game
    else:
        continue_game = True
        return f"Your roll is {roll}. Keep rolling the dice to win!", roll, continue_game
    
    

def calculate_winner(roll, throw):
    if roll == 7:
        print(f"The result of the roll was {roll}")
        print("You lost the game")
        return False
    if roll == throw:
        print(f"The result of the roll was {roll}")
        print("You won the game")
        return False
    else:
        print(f"The result of the roll was {roll}")
        print("Keep rolling")
        return True