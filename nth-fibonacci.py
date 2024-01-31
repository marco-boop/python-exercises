n = 6

def getNthFib(n):
    fibArray = []
    for i in range(n + 1):
        if i == 0:
            fibArray.append(0)
        if i == 1:
            fibArray.append(0)
        if i == 2:
            print("i is equal to 2")
            fibArray.append(1)
        if i > 2:
            print("i is: ", i)
            minusOne = fibArray[i -1]
            print("minusOne is: ", minusOne)
            minusTwo = fibArray[i-2]
            print("minusTwo is: ", minusTwo)
            fibArray.append(fibArray[i -1]+fibArray[i-2])
    print(fibArray)
    print(fibArray[n])
    return fibArray[n]
    

# def getNthFib(n):
#     if n <= 0:
#         return 0
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
#     if n > 1:
#         return(getNthFib(n-1) + getNthFib(n - 2))

answer = getNthFib(n)
print(answer)


