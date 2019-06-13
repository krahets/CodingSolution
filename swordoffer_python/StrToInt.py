# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here 
        if not s: return 0
        res, bit = 0, 1
        end = -1 if s[0] != '+' and s[0] != '-' else 0
        for i in range(len(s)-1, end, -1):
            num = ord(s[i]) - 48
            if num > 9 or num < 0: return 0
            res += num * bit
            bit *= 10
        return ~res + 1 if s[0] == "-" else res

s = Solution()
print(s.StrToInt("-12345"))

