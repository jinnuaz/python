from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        res = 0  # n xor 0 = n
        for n in nums:
            res = n ^ res
        return res

obj = Solution()
result = obj.singleNumber([1,1,2,2,3,4,4,5,5,6,7,6,8,8,7])

print(result)