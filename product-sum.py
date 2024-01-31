array = [1, 2, [3], 4, 5]
# array = [5, 2, 3, 3]


def productSum(array, depth = 1):
    finalSum = 0
    currentLevelSum = 0
    depthSum = 0
    for element in array:
        print(element)
        if type(element) == int:
            print("Printing int value: ",element)
            currentLevelSum += element
        elif type(element) == list:
            print("This is a list: ",element)
            currentLevelSum += productSum(element, depth + 1)
    multiplied = currentLevelSum * depth
    print("Multiplied: ",multiplied)
    print("depth value right now is: ",depth)

    finalSum += multiplied
    print("This is the final sum, ", finalSum)

    return finalSum





    # if all(isinstance(element, int) for element in array):
    #     print("All are int")
    #     for element in array:
    #         print("Element: ",element)
    #         depthSum += element
    #         print("DepthSum: ",depthSum)
    #     currentSum += depth * depthSum
    #     print("CurrentSum is now: ",currentSum)
    #     return depthSum
    # else:
    #     print("Not all are int")
    #     for i in range(len(array)):
    #         if type(i) is int:
    #             return productSum(i, depth + 1)


    

answer = productSum(array)
print(answer)