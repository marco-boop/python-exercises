array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
# array = [1]
# array = [-1, -5, -10, -1100, -900, -1101, -1102, -9001]
# array = [1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 11]
# array = [1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 11]
# array = [-1, -1, -1, -1, -1, -1, -1, -1]



# Below works but what's the better way?

def isMonotonic(array):
    if len(array) <= 1:
        return True
    firstPointer = 0
    secondPointer = 1
    answer = True
    while array[secondPointer] == array[firstPointer]:
        firstPointer += 1
        secondPointer += 1
        if secondPointer == len(array):
            return True
    if array[secondPointer] < array[firstPointer]:
        print("less than route")
        while secondPointer < len(array):
            print("comparing: ",array[secondPointer]," and ",array[firstPointer])
            print("secondPointer is currently ",secondPointer)
            print(array[secondPointer] > array[firstPointer])
            if array[secondPointer] > array[firstPointer]:
                answer = False
            firstPointer += 1
            secondPointer += 1
        return answer
    elif array[secondPointer] > array[firstPointer]:
        print("more than route")
        while secondPointer < len(array):
            print("comparing: ",array[secondPointer]," and ",array[firstPointer])
            print("secondPointer is currently ",secondPointer)
            print(array[secondPointer] > array[firstPointer])
            if array[secondPointer] < array[firstPointer]:
                answer = False
            firstPointer += 1
            secondPointer += 1
        return answer

a = isMonotonic(array)