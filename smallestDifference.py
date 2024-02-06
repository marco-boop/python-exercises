arrayOne = [10, 0, 20, 25, 2200]
arrayTwo = [1005, 1006, 1014, 1032, 1031]

def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    print(arrayOne)
    print(arrayTwo)
    OnePointer = 0
    TwoPointer = 0
    currentSmallest = float('inf')
    rowLowest = float('inf')
    while OnePointer <= len(arrayOne) - 1 and TwoPointer <= len(arrayTwo) - 1:
        print("Evaluating: ",OnePointer, arrayOne[OnePointer]," and on arrayTwo we are on ",TwoPointer,arrayTwo[TwoPointer])
        print(abs(arrayOne[OnePointer] - arrayTwo[TwoPointer])," versus ",rowLowest)
        if abs(arrayOne[OnePointer] - arrayTwo[TwoPointer]) <= rowLowest:
            rowLowest = abs(arrayOne[OnePointer] - arrayTwo[TwoPointer])
            if currentSmallest > rowLowest:
                print("New current smallest ___________________")
                currentSmallest = rowLowest
                answerArray = [arrayOne[OnePointer], arrayTwo[TwoPointer]]
            TwoPointer += 1
            
        elif abs(arrayOne[OnePointer] - arrayTwo[TwoPointer]) > rowLowest:
            print("current diff is larger so not continuing with this row")
            OnePointer += 1
            TwoPointer = 0
            rowLowest = float('inf')
        
    print("The current smallest diff is:",currentSmallest)
    print(answerArray)
    return answerArray

a = smallestDifference(arrayOne, arrayTwo)
print(a)