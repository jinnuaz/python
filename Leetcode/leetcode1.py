from Leetcode.leetcode_twosum import hashMap

nums = [2, 7, 11, 15]
target = 9
hashMap = {}

def TwoSum(nums, target):
    for i in range(len[nums]):
        diff = target - nums[i]
        if diff in hashMap:
            return hashMap[diff], i
        hashMap[nums[i]] = i

print(TwoSum(nums, target))



