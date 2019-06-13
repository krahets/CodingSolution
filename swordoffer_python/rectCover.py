# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number == 0 or number == 1:
            return number
        a=0
        b=1
        for _ in range(number):
            a,b = b,a+b
        return b