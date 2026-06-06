

nums = [2, 7, 11, 15]
target = 9
hash_Map = {}

def TwoSum(nums, target):
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in hash_Map:
            return hash_Map[diff], i
        hash_Map[nums[i]] = i

print(TwoSum(nums, target))



