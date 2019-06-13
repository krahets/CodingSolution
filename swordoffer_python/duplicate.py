# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        table = [0 for _ in range(len(numbers))]
        for n in numbers:
            if table[n] > 0:
                duplication[0] = n
                return True
            table[n] += 1
        return False