array = [-2, -1, 7]

def findThreeLargestNumbers(array):
    output = [float("-inf")] * 3
    for i in range(len(array)):
        print("Evaluating: ",i, array[i])
        if array[i] > output[2]:
            print("A")
            output[0] = output[1]
            output[1] = output[2]
            output[2] = array[i]
            print(output)
        elif array[i] > output[1]:
            print("B")
            output[0] = output[1]
            output[1] = array[i]
            print(output)
        elif array[i] > output[0]:
            print("C")
            output[0] = array[i]
            print(output)
        else:
            print("D")
            print("Current evaluated value did not make the cut")
    print(output)
    return output

answer = findThreeLargestNumbers(array)