# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        res, exp = 1, abs(exponent)
        while exp != 0:
            if exp & 1 != 0: res *= base
            base *= base
            exp >>= 1
        return res if exponent > 0 else 1/res