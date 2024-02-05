array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0

def threeNumberSum(array, targetSum):
    mainArray = []
    array.sort()
    numberSet = set(array)
    print(numberSet)
    for number in array:
        print(mainArray)
        for i in range(len(array)):
            currentThree = []
            lastOne = targetSum - number - array[i]
            if array[i] != number and lastOne != number and lastOne != array[i] and lastOne in numberSet:
                currentThree.append(number)
                currentThree.append(array[i])
                currentThree.append(lastOne)
                currentThree.sort()
                print("Found three",currentThree)
            if currentThree != [] and currentThree not in mainArray:
                print("Appending array to mainArray",mainArray)
                mainArray.append(currentThree)
                print(mainArray)
    print(mainArray)

answer = threeNumberSum(array, targetSum)
print(answer)