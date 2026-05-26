
# nums = [1,2,3,1]
nums = [1,2,3,4]
def containsDuplicate(nums):
    hashset = set()

    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False

print(containsDuplicate(nums))
