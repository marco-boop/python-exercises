array = [8, 5, 2, 9, 5, 6, 3]

def insertionSort(array):
    anySwapsies = True
    
    while anySwapsies is True:
        currentSwapsies = False
        for i in range(1, len(array)):
            
            # print("Currently our number is",i," , ",array[i])

            current = array[i]
            # print("Comparing: ",array[i]," versus ",array[i - 1])
            if array[i] > array[i - 1]:
                print(array[i]," is larger than ",array[i - 1])
                # print("No changes")
            elif array[i] < array[i - 1]:
                # print("SWAPPPPP")
                currentSwapsies = True
                array[i] = array[i - 1]
                array[i - 1] = current

        anySwapsies = currentSwapsies
    print(array)
    return array

answer = insertionSort(array)