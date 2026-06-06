nums = [2, 7, 11, 15]
target = 9

def bruteforce_twosum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                print(f"sum of two sums = target are {nums[i]} and {nums[j]} and their indices are {i} and {j}")
                return i, j, nums[i], nums[j]

result = bruteforce_twosum(nums, target)
print(result)
