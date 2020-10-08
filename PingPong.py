def check_pingpong_winner(tupleScores):
    if (tupleScores[0] >= 21 or tupleScores[1] >= 21):
        if (tupleScores[0] >= 21 and tupleScores[0]-tupleScores[1] >= 2):
            return ("Player 1 wins!")
        elif(tupleScores[1] >= 21 and tupleScores[1]-tupleScores[0] >= 2):
            return("Player 2 wins!")
        else:
            return("Keep playing!")

    else:
        return("Keep playing!")


print(check_pingpong_winner((25,27)))