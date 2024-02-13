# seats = [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1]
seats = [1, 1, 1]

def bestSeat(seats):
    bestSeat = -1
    longestSpace = 0
    leftPointer = 0
    rightPointer = 1
    while rightPointer < len(seats):
        print(leftPointer," and ", rightPointer)
        if seats[leftPointer] == 1 and seats[rightPointer] == 1:
            currentDistance = rightPointer - leftPointer - 1
            if currentDistance > longestSpace:
                longestSpace = currentDistance
                bestSeat = (leftPointer + rightPointer) // 2
            leftPointer = rightPointer
            rightPointer = leftPointer + 1
        else:
            rightPointer += 1
    print("best seat at the end", bestSeat)
    return bestSeat


# def bestSeat(seats):
#     longest = 0
#     current = 0
#     endOfLongestIndex = 0
#     currentStart = None
#     startoflongest = None
#     for i in range(len(seats)):
#         if seats[i] == 1:
#             current = 0
#             currentStart = i + 1
#         if seats[i] == 0:
#             current += 1
#             if currentStart is None:
#                 currentStart = i
#         if current > longest:
#             longest = current
#             endOfLongestIndex = i
#             startoflongest = currentStart
#     print("Longest segment is: ",longest)
#     print("endOfLongestIndex is: ",endOfLongestIndex)
#     print("startoflongest is: ",startoflongest)
#     if longest % 2 != 0:
#         middle = (longest // 2) + 1
#     else:
#         middle = longest //2

#     print("MIddle is: ", middle)

#     print("Is this the answer: ",endOfLongestIndex - middle + 1)

#     if endOfLongestIndex == 0:
#         return -1
#     elif longest == 2:
#             selectedSeat = endOfLongestIndex - 1
#     else:
#         if longest % 2 == 0:
#             selectedSeat = endOfLongestIndex - middle
#         else:        
#             selectedSeat = endOfLongestIndex - middle + 1
    
#     return selectedSeat

answer = bestSeat(seats)
print(answer)