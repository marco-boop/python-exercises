competitions = [
    ["HTML","C#"],
    ["C#","Python"],
    ["Python","HTML"],
]

results = [0,0,1]

# def tournamentWinner(competitions, results):
#     wins = {}
#     # print(wins)
#     for faceOff in range(len(results)):
#         # print(results[faceOff])
#         if results[faceOff] == 0:
#             winningTeam = competitions[faceOff][1]
#             if winningTeam in wins:
#                 wins[winningTeam] += 1
#             else:
#                 wins[winningTeam] = 1
#             # print(wins)
#         else:
#             winningTeam = competitions[faceOff][0]
#             if winningTeam in wins:
#                 wins[winningTeam] += 1
#             else:
#                 wins[winningTeam] = 1
#             # print(wins)
    
#     tournWinner = max(wins, key=wins.get)
#     print("The winner is ", tournWinner)
#     return tournWinner

# def tournamentWinner(competitions, results):
#     wins = {}
#     for faceOff in range(len(results)):
#         if results[faceOff] == 0:
#             winningTeam = competitions[faceOff][1]
#             if winningTeam in wins:
#                 wins[winningTeam] += 1
#             else:
#                 wins[winningTeam] = 1
#         else:
#             winningTeam = competitions[faceOff][0]
#             if winningTeam in wins:
#                 wins[winningTeam] += 1
#             else:
#                 wins[winningTeam] = 1
#     tournWinner = max(wins, key=wins.get)
#     return tournWinner

def tournamentWinner(competitions, results):
    wins = {}
    finalWinner = "no one"
    for faceOff in range(len(results)):
        if results[faceOff] == 0:
            winningTeam = competitions[faceOff][1]
            if winningTeam in wins:
                wins[winningTeam] += 3
            else:
                wins[winningTeam] = 3
        else:
            winningTeam = competitions[faceOff][0]
            if winningTeam in wins:
                wins[winningTeam] += 3
            else:
                wins[winningTeam] = 3
        print("Most recent winner is ",winningTeam)
        print(wins)
        print(finalWinner)
        if finalWinner == "no one":
            finalWinner = winningTeam
            print("First final winner is ", finalWinner)
        else:
            print("Current final winner name is ", finalWinner," and their score is ", wins[finalWinner])
            print("Challenger winner name is ", winningTeam," and their score is ", wins[winningTeam])
            if wins[winningTeam] > wins[finalWinner]:
                print("final winner replaced by ", winningTeam)
                finalWinner = winningTeam
    # tournWinner = max(wins, key=wins.get)
    return finalWinner


answer = tournamentWinner(competitions, results)
print(answer)