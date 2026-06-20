class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        # Defining two pointers

        i = len(s) - 1      # Pointer 1
        length = 0          # Pointer 2
        while s[i] == " ":
            i = i - 1
        while i >= 0 and s[i] != " ":
            length = length + 1
            i = i - 1
        return length


obj = Solution()
result = obj.lengthOfLastWord(" dfgdfg dfgdsfgd dfgdfgfgf  ")
print(result)