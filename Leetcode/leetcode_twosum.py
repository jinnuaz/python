nums = [2,7,11,15]
target = 9
hashMap = {}

def solution(nums):
    for i, n in enumerate(nums):
        diff = target - n
        if diff in hashMap:
            return [hashMap[diff], i]

        else:
            hashMap[n] = i

print(f"Two sum results is {solution(nums)}")