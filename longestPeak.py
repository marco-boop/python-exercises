# array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
array = [1, 3, 2]

def longestPeak(array):
    longestPeak = 0
    direction = None
    for i in range(1,len(array)):
        print("----- Current on: ",array[i]," in position ",i," and we going", direction)
        if direction == None:
            if array[i] > array[i - 1]:
                currentPeak = 2
                print("Current peak add 1")
                print(currentPeak)
                direction = "up"
            if array[i] <= array[i - 1]:
                currentPeak = 1
                direction = None
        elif direction == "up":
            if array[i] > array[i - 1]:
                print("UP - Comparing: ",array[i]," and ",array[i - 1])
                currentPeak +=1
                direction = "up"
            if array[i] < array[i - 1]:
                currentPeak += 1
                direction = "down"
                print("complete peak")
            if array[i] == array[i - 1]:
                if currentPeak > longestPeak:
                    longestPeak = currentPeak
                currentPeak = 1
                direction = None
        elif direction == "down":
            if array[i] >= array[i - 1]:
                if currentPeak > longestPeak:
                    longestPeak = currentPeak
                currentPeak = 2
                direction = "up"
            if array[i] < array[i - 1]:
                currentPeak +=1
                direction = "down"
    if currentPeak > longestPeak:
        longestPeak = currentPeak
        
    return longestPeak

a = longestPeak(array)
print(a)