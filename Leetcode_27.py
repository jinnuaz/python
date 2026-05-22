nums = [0,1,2,2,7,4,6,2,4,5,6,3,0,4,2]
val = 2

def solution(nums):
    k = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1

    return k

print(solution(nums))