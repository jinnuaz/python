nums = [1,3,4,5,7,10,11]
target = 9
 #7

def solution(nums):
    left = 0
    right = len(nums)-1
    while(left < right):
        if (nums[left] + nums[right] > target):
            right = right -1
        elif(nums[left] + nums[right] < target):
            left = left +1
        else :
            return[left+1,right+1]

print(solution(nums))