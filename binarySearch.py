import math

array = [1, 5, 23, 111]
target = 120

import math

def binarySearch(array, target, start = 0, end = None):

    if end is None:
         end = len(array)

    halfIndex = start + math.floor((end - start) / 2)

    if start > end:
         return -1

    if halfIndex > len(array) - 1:
        return -1
    
    if array[halfIndex] == target:
        return halfIndex
    elif array[halfIndex] > target:
         return binarySearch(array, target, start, halfIndex - 1)
    else:
         return binarySearch(array, target, halfIndex + 1, end)

# def binarySearch(array, target, halfIndex = None):

#     def findMiddle(array):
#         bottom = 0
#         top = len(array) - 1
#         midpoint = math.floor((bottom + top) / 2)
#         print(midpoint)
#         print(array[midpoint])
    
#     findMiddle(array)

def binarySearch(array, target, start = 0, end = None):

    if end is None:
         end = len(array)

    halfIndex = start + math.floor((end - start) / 2)
    print("Start is: ",start)
    print("End is: ",end)
    print("Half index is: ",halfIndex)

    if start > end:
        return -1
    
    if halfIndex > len(array) - 1:
        return -1
    
    if array[halfIndex] == target:
        return halfIndex
    elif array[halfIndex] > target:
         print("On the left: New half index is: ")
         return binarySearch(array, target, start, halfIndex - 1)
    else:
         print("Current is smaller so going right: New half index is: ")
         return binarySearch(array, target, halfIndex + 1, end)

answer = binarySearch(array, target)
print(answer)