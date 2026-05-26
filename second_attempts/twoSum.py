
# nums    = [2,7,11,15]
# target  = 9

nums    = [3,2,4]
target  = 6
def twoSum(nums):

    hashMap = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in hashMap:
            return [hashMap[diff], i]

        hashMap[n] = i
    return []

print(twoSum(nums))