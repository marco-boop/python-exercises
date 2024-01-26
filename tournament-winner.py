competitions = [
    ["HTML","C#"],
    ["C#","Python"],
    ["Python","HTML"],
]

results = [0,0,1]

def tournamentWinner(competitions, results):
    wins = {}
    # print(wins)
    for faceOff in range(len(results)):
        # print(results[faceOff])
        if results[faceOff] == 0:
            winningTeam = competitions[faceOff][1]
            if winningTeam in wins:
                wins[winningTeam] += 1
            else:
                wins[winningTeam] = 1
            # print(wins)
        else:
            winningTeam = competitions[faceOff][0]
            if winningTeam in wins:
                wins[winningTeam] += 1
            else:
                wins[winningTeam] = 1
            # print(wins)
    
    tournWinner = max(wins, key=wins.get)
    print("The winner is ", tournWinner)
    return tournWinner

answer = tournamentWinner(competitions, results)
print(answer)