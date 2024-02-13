array = [1,2,3,4,5,6,10,20]
k = 5

def sumDivisibleByK(array):
    count = 0
    dict = {}
    for i in range(k):
        dict[i] = 0
    for i in range(len(array)):
        remainder = array[i] % k
        dict[remainder] += 1
    print(dict)
    #     if remainder in dict:
    #         count += 1
    # return count

# def sumDivisibleByK(array):
#     count = 0
#     for i in range(len(array)):
#         for j in range(i + 1, len(array)):
#             print(array[i], array[j])
#             if i != j and (array[i] + array[j]) % 3 == 0:
#                 count += 1
#     return count

answer = sumDivisibleByK(array)
print(answer)