

nums = [1,3,5,6]
target = 5

def searchInsert(nums):

    left    = 0
    right   = len(nums)-1


    while(left < right):
        middle = int(left + right//2)
        if target == nums[middle]:
            return middle

        elif target > nums[middle] :
            left = middle + 1

        else:
            right = middle - 1

    return left

print(f"position of {target} is {searchInsert(nums)}")