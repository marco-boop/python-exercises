array = [8, 5, 2, 9, 5, 6, 3]

def bubbleSort(array):
    
    def swap(array, indexA, indexB):
        placeholder = array[indexA]
        array[indexA] = array[indexB]
        array[indexB] = placeholder
    
    swapHappened = True
    
    while swapHappened == True:
        swapHappened = False
        for i in range(1, len(array)):
            if array[i-1] > array[i]:
                swap(array, i-1, i)
                swapHappened = True
    return array

answer = bubbleSort(array)


# Clean
# def bubbleSort(array):
#     swapsies = False
#     while swapsies is False:
#         noChanges = True
#         for i in range(len(array)):
#             if i < len(array) - 1:
#                 currentValue = array[i]
#                 if currentValue > array[i + 1]:
#                     noChanges = False
#                     array[i] = array[i + 1]
#                     array[i + 1] = currentValue
#             swapsies = noChanges    
#     return array

# def bubbleSort(array):
#     swapsies = False
#     print("This array has",len(array),"locations")
#     while swapsies is False:
#         # I needed to move this out of the for loop
#         noChanges = True
#         for i in range(len(array)):
#             print("i is: ",i)
#             if i < len(array) - 1:
#                 print(array[i])
#                 currentValue = array[i]


#                 if currentValue > array[i + 1]:
#                     print("Swap happening so noChanges will become true")
#                     noChanges = False
#                     array[i] = array[i + 1]
#                     array[i + 1] = currentValue

#             swapsies = noChanges    
#     print(array)
#     return array

# answer = bubbleSort(array)