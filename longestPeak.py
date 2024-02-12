# array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
array = [1, 3, 2]

def longestPeak(array):
    longestPeak = 0
    for i in range(1,len(array)-1):
        if array[i] > array[i - 1] and array[i] > array[i + 1]:
            base = 3
            leftSide = 0
            current = i - 1
            oneLess = i - 2
            while array[current] > array[oneLess]:
                leftSide += 1
                current -= 1
                oneLess -= 1
            rightSide = 0
            currentRight = i + 1
            oneMore = i + 2
            while oneMore < len(array) and array[currentRight] > array[oneMore]:
                rightSide += 1
                currentRight += 1
                oneMore += 1
            currentPeak = base + leftSide + rightSide
            if currentPeak > longestPeak:
                longestPeak = currentPeak

    return longestPeak

# # treat every integer as a peak

# def longestPeak(array):
#     longestPeak = 0
#     for i in range(1,len(array)-1):
#         if array[i] > array[i - 1] and array[i] > array[i + 1]:
#             print("peak found: ",array[i]," at index ",i)
#             base = 3
#             leftSide = 0
#             current = i - 1
#             oneLess = i - 2
#             while array[current] > array[oneLess]:
#                 print("left")
#                 leftSide += 1
#                 current -= 1
#                 oneLess -= 1
            
#             # going down on the right
#             rightSide = 0
#             currentRight = i + 1
#             oneMore = i + 2
#             while oneMore < len(array) and array[currentRight] > array[oneMore]:
#                 print("right")
#                 rightSide += 1
#                 currentRight += 1
#                 oneMore += 1

#             currentPeak = base + leftSide + rightSide
#             if currentPeak > longestPeak:
#                 longestPeak = currentPeak

#     return longestPeak





    #     print("----- Current on: ",array[i]," in position ",i," and we going", direction)
    #     if direction == None:
    #         if array[i] > array[i - 1]:
    #             currentPeak = 2
    #             print("Current peak add 1")
    #             print(currentPeak)
    #             direction = "up"
    #         if array[i] <= array[i - 1]:
    #             currentPeak = 1
    #             direction = None
    #     elif direction == "up":
    #         if array[i] > array[i - 1]:
    #             print("UP - Comparing: ",array[i]," and ",array[i - 1])
    #             currentPeak +=1
    #             direction = "up"
    #         if array[i] < array[i - 1]:
    #             currentPeak += 1
    #             direction = "down"
    #             print("complete peak")
    #         if array[i] == array[i - 1]:
    #             if currentPeak > longestPeak:
    #                 longestPeak = currentPeak
    #             currentPeak = 1
    #             direction = None
    #     elif direction == "down":
    #         if array[i] >= array[i - 1]:
    #             if currentPeak > longestPeak:
    #                 longestPeak = currentPeak
    #             currentPeak = 2
    #             direction = "up"
    #         if array[i] < array[i - 1]:
    #             currentPeak +=1
    #             direction = "down"
    # if currentPeak > longestPeak:
    #     longestPeak = currentPeak
    # return longestPeak

# def longestPeak(array):
#     longestPeak = 0
#     direction = None
#     for i in range(1,len(array)):
#         print("----- Current on: ",array[i]," in position ",i," and we going", direction)
#         if direction == None:
#             if array[i] > array[i - 1]:
#                 currentPeak = 2
#                 print("Current peak add 1")
#                 print(currentPeak)
#                 direction = "up"
#             if array[i] <= array[i - 1]:
#                 currentPeak = 1
#                 direction = None
#         elif direction == "up":
#             if array[i] > array[i - 1]:
#                 print("UP - Comparing: ",array[i]," and ",array[i - 1])
#                 currentPeak +=1
#                 direction = "up"
#             if array[i] < array[i - 1]:
#                 currentPeak += 1
#                 direction = "down"
#                 print("complete peak")
#             if array[i] == array[i - 1]:
#                 if currentPeak > longestPeak:
#                     longestPeak = currentPeak
#                 currentPeak = 1
#                 direction = None
#         elif direction == "down":
#             if array[i] >= array[i - 1]:
#                 if currentPeak > longestPeak:
#                     longestPeak = currentPeak
#                 currentPeak = 2
#                 direction = "up"
#             if array[i] < array[i - 1]:
#                 currentPeak +=1
#                 direction = "down"
#     if currentPeak > longestPeak:
#         longestPeak = currentPeak
        
#     return longestPeak

a = longestPeak(array)
print(a)