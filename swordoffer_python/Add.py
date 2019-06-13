# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        # write code here
        while num2:
            num1, num2 = (num1 ^ num2) & 0xFFFFFFFF, ((num1 & num2) << 1) & 0xFFFFFFFF
        return num1 if num1 <= 0x7FFFFFFF else ~(num1 ^ 0xFFFFFFFF)

s = Solution()
print(s.Add(1, -2))