
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber > 0:
            offset = (columnNumber-1) % 26
            res = res + chr(ord('A') + offset)
            columnNumber = (columnNumber - 1) // 26

        return res[::-1]

obj = Solution()
result = obj.convertToTitle(701)
print(result)
