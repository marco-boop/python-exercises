queries = [3, 2, 1, 2, 6]

def minimumWaitingTime(queries):
    queries.sort()
    for i in range(len(queries)):
        if i == 0:
            waitingTime = 0
            totalSum = 0
        else:
            print("The current is: ",queries[i])
            print("The previous is: ",queries[i - 1])
            waitingTime = waitingTime + queries[i - 1]
            print("New waiting time is: ",waitingTime)
            totalSum += waitingTime
    return totalSum

answer = minimumWaitingTime(queries)
print("Final answer: ", answer)
