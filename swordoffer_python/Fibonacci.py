# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0 or n == 1:
            return n
        a=0
        b=1
        for _ in range(n-1):
            a,b = b,a+b
        return b