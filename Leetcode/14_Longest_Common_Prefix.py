

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        res = ""

        for i in range(len(strs[0])):
            for s in strs:
                if s[i] != s[0][i]:
                    return res
            res = res + s[0][i]
        return res

obj = Solution()
result = obj.longestCommonPrefix(["flower","flow","flight"])