def find_winner(lsOfTuples):
    player1Wins = 0
    player2Wins = 0
    for i in lsOfTuples:
        if (i[0] == i[1]):
            pass
        elif (i[0] == "Rock"):
            if (i[1] == "Scissors"):
                player1Wins = player1Wins + 1
            else:
                player2Wins = player2Wins + 1
        elif(i[0] == "Scissors"):
            if (i[1] == "Paper"):
                player1Wins = player1Wins + 1
            else:
                player2Wins = player2Wins + 1
        elif(i[0] == "Paper"):
            if(i[1] == "Rock"):
                player1Wins = player1Wins + 1
            else:
                player2Wins = player2Wins + 1

    if (player2Wins > player1Wins):
        return ("Player 2 wins!")
    elif (player1Wins > player2Wins):
        return ("Player 1 wins!")
    else:
        return ("It's a tie!")


p1_wins = [("Rock", "Rock"), ("Rock", "Scissors"), ("Paper", "Rock"), ("Scissors", "Rock")]
p2_wins = [("Paper", "Rock"), ("Paper", "Paper"), ("Paper", "Scissors"), ("Rock", "Paper")]
itsatie = [("Paper", "Paper"), ("Paper", "Rock"), ("Rock", "Paper"), ("Scissors", "Scissors")]

print(find_winner(p2_wins))


