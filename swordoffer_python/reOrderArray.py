# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        odd, even = [], []
        for a in array:
            odd.append(a) if a & 1 else even.append(a)
        return odd + even