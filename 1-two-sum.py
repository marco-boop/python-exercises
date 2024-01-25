nums = [2, 7, 11, 15]
target = 9

def two_sums(nums, target, i=0):
    if i >= len(nums):
        return None
    
    for j in range(len(nums)):
        if i != j and nums[i] + nums[j] == target:
            return [i, j]
        
    return two_sums(nums, target, i + 1)

answer = two_sums(nums, target)
print(answer)