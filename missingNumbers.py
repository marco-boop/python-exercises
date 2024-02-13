# nums = [1, 4, 3]
nums = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# This did not feel simpler but better in terms of space

def missingNumbers(nums):
    n = len(nums) + 2
    sumOfNValues = 0
    currentSum = sum(nums)
    print("Current sum is: ",currentSum)
    for i in range(1,n + 1):
        sumOfNValues += i
        print(sumOfNValues)
    missingDifference = sumOfNValues - currentSum
    print("The missing diff is: ",missingDifference)
    half = missingDifference // 2
    print("HALF",half)
    leftSum = 0
    rightSum = 0
    for i in range(len(nums)):
        print("New",i,nums[i])
        if nums[i] <= half:
            leftSum += nums[i]
        else:
            rightSum += nums[i]
    
    rightTotal = 0
    leftTotal = 0
    for i in range(1,n + 1):
        if i <= half:
            leftTotal += i
        else:
            rightTotal += i
    print(leftSum,leftTotal)
    print(rightSum,rightTotal)
    missing = [(leftTotal - leftSum),(rightTotal - rightSum)]
    print(missing)

# def missingNumbers(nums):
#     missing = []
#     n = len(nums) + 2
#     myset = set(nums)
#     for i in range(1,n + 1):
#         print(i)
#         if i not in myset:
#             missing.append(i)
#     print(missing)

answer = missingNumbers(nums)
print(answer)
