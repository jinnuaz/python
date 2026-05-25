

nums = [-2,1,-3,4,-1,2,1,-5,4]
def maxSubArray(nums):

    maxSub  = nums[0]
    currSum = 0

    for n in nums:
        if currSum < 0:
            currSum = 0

        currSum = currSum + n
        maxSub = max(maxSub, currSum)
        print(f"for n = {n} - maxSub = {maxSub}")

    return maxSub

print(maxSubArray(nums))
