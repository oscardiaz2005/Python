def rock_paper_scissors(player1, player2):
    score_player1 = 0
    score_player2 = 0

    for i in range(3):
        print(f"\nRound {i+1}:")
        move_player1 = input(f"{player1}, choose rock, paper, or scissors: ").lower()
        move_player2 = input(f"{player2}, choose rock, paper, or scissors: ").lower()

        if move_player1 == move_player2:
            print("It's a tie in this round.")
        elif (move_player1 == "rock" and move_player2 == "scissors") or \
             (move_player1 == "paper" and move_player2 == "rock") or \
             (move_player1 == "scissors" and move_player2 == "paper"):
            print(f"{player1} wins this round.")
            score_player1 += 1
        else:
            print(f"{player2} wins this round.")
            score_player2 += 1

    if score_player1 > score_player2:
        return player1, score_player1 * 10
    elif score_player2 > score_player1:
        return player2, score_player2 * 10
    else:
        return "Tie", 0