array = [5, -2, 2, -8, 3, -10, -6, -1, 2, -2, 9, 1, 1]

def selectionSort(array):

    def swap(array,a,b):
        array[a], array[b] = array[b], array[a]
        return array

    for i in range(len(array)):
        print("Outside: ",array[i],"----------------------")
        smolIndex = i
        for j in range(i + 1, len(array)):
            if i != smolIndex:
                if array[smolIndex] > array[j]:
                    print("new smol is ",array[j]," at index ",j)
                    smolIndex = j
                    print("did smolIndex update?",smolIndex)
            else:
                if array[i] > array[j]:
                    print("new smol is ",array[j]," at index ",j)
                    smolIndex = j
                    print("did smolIndex update?",smolIndex)
        swap(array, i, smolIndex)

    return array

answer = selectionSort(array)
print(answer)