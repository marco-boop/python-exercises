array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2

# Below works but can be improved swapping values instead of deleting and appending

def moveElementToEnd(array, toMove):

    def swap(array,leftIndex, rightIndex):
        holder = array[leftIndex]
        array[leftIndex] = array[rightIndex]
        array[rightIndex] = holder
        return array

    leftPointer = 0
    rightPointer = len(array) - 1
    if array == []:
        return []
    while leftPointer != rightPointer:
        current = array[leftPointer]
        if current == toMove:
            swap(array, leftPointer, rightPointer)
            rightPointer -= 1
        else:
            leftPointer += 1
    return array


# Telling me I can solve with two pointers

# def moveElementToEnd(array, toMove):
#     leftPointer = 0
#     rightPointer = len(array) - 1
#     print("The pointers are: ",leftPointer," and ",rightPointer)
#     if array == []:
#         return []
#     while leftPointer != rightPointer:
#         current = array[leftPointer]
#         if current == toMove:
#             array.append(toMove)
#             del array[leftPointer]
#             rightPointer -= 1
#         else:
#             leftPointer += 1
#       return array


    # for i in range(len(array)):
    #     if array[i] == toMove:
    #         print(array[i])
    #         toMoveArray.append(i)
    # print(toMoveArray)
    # addAtTheEnd = len(toMoveArray)
    # for j in range(len(toMoveArray) - 1, -1, -1):
    #     # print(array[toMoveArray[j]])
    #     del array[toMoveArray[j]]
    #     print(array)
    # print("add at the end is: ",addAtTheEnd)
    # while addAtTheEnd != 0:
    #     print("Inside: add at the end is: ",addAtTheEnd)
    #     array.append(toMove)
    #     addAtTheEnd -= 1
    # return array

# Passed

# def moveElementToEnd(array, toMove):
#     toMoveArray = []
#     for i in range(len(array)):
#         if array[i] == toMove:
#             print(array[i])
#             toMoveArray.append(i)
#     print(toMoveArray)
#     addAtTheEnd = len(toMoveArray)
#     for j in range(len(toMoveArray) - 1, -1, -1):
#         # print(array[toMoveArray[j]])
#         del array[toMoveArray[j]]
#         print(array)
#     print("add at the end is: ",addAtTheEnd)
#     while addAtTheEnd != 0:
#         print("Inside: add at the end is: ",addAtTheEnd)
#         array.append(toMove)
#         addAtTheEnd -= 1
#     return array

a = moveElementToEnd(array, toMove)
print(a)