nums = [2, 7, 11, 15]
target = 9

def bruteforce_twosum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j, nums[i], nums[j]

result = bruteforce_twosum(nums, target)
print(f"sum of two sums = target are {result[2]} and {result[3]} and their indices are {result[0]} and {result[1]}")
