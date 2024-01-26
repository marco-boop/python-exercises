array = [-3, -2, -1]
    
# def sortedSquaredArray(array):
#     newArray = []
#     firstValue = 0
#     print("first value is ",firstValue)
#     lastValue = len(array) - 1
#     print("last value is ", lastValue)
#     while firstValue != lastValue:
#         if abs(array[firstValue]) > abs(array[lastValue]):
#             newArray.insert(0, array[firstValue] * array[firstValue])
#             firstValue += 1
#             # print(newArray)
#             print("new first value is ",firstValue)
#         elif abs(array[firstValue]) < abs(array[lastValue]):
#             newArray.insert(0, array[lastValue] * array[lastValue])
#             lastValue -= 1
#             print("new last value is ",lastValue)
#     if firstValue == lastValue:
#         newArray.insert(0, array[firstValue] * array[firstValue])
#     return newArray

def sortedSquaredArray(array):
    newArray = []
    firstValue = 0
    lastValue = len(array) - 1
    while firstValue <= lastValue:
        if abs(array[firstValue]) > abs(array[lastValue]):
            newArray.insert(0, array[firstValue] * array[firstValue])
            firstValue += 1
        elif abs(array[firstValue]) <= abs(array[lastValue]):
            newArray.insert(0, array[lastValue] * array[lastValue])
            lastValue -= 1
    if firstValue == lastValue:
        newArray.insert(0, array[firstValue] * array[firstValue])
    return newArray

answer = sortedSquaredArray(array)
print(answer)

