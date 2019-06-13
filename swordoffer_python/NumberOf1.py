# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        n &= 0xffffffff
        count = 0
        while n:
            count += 1
            n = n & (n-1) 
        return count