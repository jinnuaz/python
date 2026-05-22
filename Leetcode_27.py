nums = [0,1,2,2,3,0,4,2]
val = 2

def solution(nums):
    k = 0

    for i in range(nums):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1

    return k

print(solution(nums))