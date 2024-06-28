from procesos.procesos_exercise8 import *
# Ask for players' names
player1 = input("Enter the name of the first player: ")
player2 = input("Enter the name of the second player: ")

# Play the game and get the result
winner, score = rock_paper_scissors(player1, player2)

# Display the result
print("\nThe winner is:", winner)
print("Score:", score)