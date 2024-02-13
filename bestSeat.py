seats = [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1]

def bestSeat(seats):
    longest = 0
    current = 0
    endOfLongestIndex = 0
    for i in range(len(seats)):
        if seats[i] == 1:
            current = 0
        if seats[i] == 0:
            current += 1
        if current > longest:
            longest = current
            endOfLongestIndex = i
    print("Longest segment is: ",longest)
    print("endOfLongestIndex is: ",endOfLongestIndex)
    if longest % 2 != 0:
        middle = (longest // 2) + 1
    else:
        middle = longest //2

    print("MIddle is: ", middle)

    print("Is this the answer: ",endOfLongestIndex - middle + 1)

    if endOfLongestIndex == 0:
        return -1
    elif longest == 2:
            selectedSeat = endOfLongestIndex - 1
    else:
        if longest % 2 == 0:
            selectedSeat = endOfLongestIndex - middle
        else:        
            selectedSeat = endOfLongestIndex - middle + 1
    
    return selectedSeat

answer = bestSeat(seats)
print(answer)