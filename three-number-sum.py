array = [1, 2, 3]
targetSum = 6

# array = [12, 3, 1, 2, -6, 5, -8, 6]
# targetSum = 0

# Gonna try with pointers instead

def threeNumberSum(array, targetSum):
    mainArray = []
    array.sort()
    for i in range(len(array)-1):
        currentNumber = array[i]
        leftPointer = i + 1
        rightPointer = len(array)-1
        while leftPointer < rightPointer:
            print("Current",currentNumber)
            print("Left",array[leftPointer])
            print("Right",array[rightPointer])
            print("Sum is: ", currentNumber + array[leftPointer] + array[rightPointer])
            if currentNumber + array[leftPointer] + array[rightPointer] == targetSum and array[leftPointer] != array[rightPointer]:
                currentThree = [currentNumber, array[leftPointer], array[rightPointer]]
                print(currentThree)
                mainArray.append(currentThree)
            if currentNumber + array[leftPointer] + array[rightPointer] > targetSum:
                rightPointer -= 1
            elif currentNumber + array[leftPointer] + array[rightPointer] <= targetSum:
                leftPointer += 1
            
    return mainArray

# This works

# def threeNumberSum(array, targetSum):
#     mainArray = []
#     array.sort()
#     numberSet = set(array)
#     for number in array:
#         for i in range(len(array)):
#             currentThree = []
#             lastOne = targetSum - number - array[i]
#             if array[i] != number and lastOne != number and lastOne != array[i] and lastOne in numberSet:
#                 currentThree.append(number)
#                 currentThree.append(array[i])
#                 currentThree.append(lastOne)
#                 currentThree.sort()
#             if currentThree != [] and currentThree not in mainArray:
#                 mainArray.append(currentThree)
#     return mainArray

answer = threeNumberSum(array, targetSum)
print(answer)