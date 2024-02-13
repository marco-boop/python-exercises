# nums = [-5, -5, 2, 3, -2]
# nums = [2, -2]
nums = [1, 2, 3, 4, 0, 5, 6, 7]

def zeroSumSubarray(nums):
    sums = set([0])
    runningCount = 0
    for i in range(len(nums)):
        runningCount += nums[i]
        if runningCount in sums:
            print("Checking for: ",runningCount)
            return True
        sums.add(runningCount)
        print(sums)
    return False

# def zeroSumSubarray(nums):
    zeroFound = True
    dict = {}
    runningCount = 0
    if len(nums) == 1 and nums[0] == 0:
        return True
    
    for i in range(len(nums)):
        print("Currently on: ",nums[i])
        checkingForDupe = nums[i] + runningCount
        if checkingForDupe in dict.values() or checkingForDupe == 0:
            return True
        if i == 0:
            dict[i] = nums[i]
            print(dict)
            runningCount += nums[i]
        else:
            dict[i] = nums[i] + runningCount
            runningCount += nums[i]
    return False

answer = zeroSumSubarray(nums)
print(answer)