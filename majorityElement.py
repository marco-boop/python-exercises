array = [1, 2, 3, 2, 2, 1, 2]
# array = [2]
# array = [3, 3, 1]

def majorityElement(array):
    for i in range(len(array)):
        counter = 1
        if counter == 0:
            break
        for j in range(len(array)):
            if array[i] == array[j]:
                counter += 1
            else:
                counter -= 1
        if counter > 1:
            return array[i]
    return -1

answer = majorityElement(array)
print(answer)


    # if len(array) == 1:
    #     return array[0]
    # for i in range(len(array)):
    #     array[0] += 0.1
    #     # print(int(array[i]), array[i])
    #     array[int(array[i])] += 0.1
    # for i in range(1, len(array)):
    #     currentIndexSum = int(100*(array[i] - int(array[i])))
    #     totalSum = int(100*(array[0] - int(array[0])))
    #     print(currentIndexSum, totalSum)
    #     print(currentIndexSum/totalSum)
    #     if currentIndexSum/totalSum > 0.5:
    #         print(i)
    #         return i
    # return -1

# This only works when the values in the array have a corresponding index
# So not a good solution so far: 9/14

# def majorityElement(array):
#     if len(array) == 1:
#         return array[0]
#     for i in range(len(array)):
#         array[0] += 0.1
#         # print(int(array[i]), array[i])
#         array[int(array[i])] += 0.1
#     for i in range(1, len(array)):
#         currentIndexSum = int(100*(array[i] - int(array[i])))
#         totalSum = int(100*(array[0] - int(array[0])))
#         print(currentIndexSum, totalSum)
#         print(currentIndexSum/totalSum)
#         if currentIndexSum/totalSum > 0.5:
#             print(i)
#             return i
#     return -1

