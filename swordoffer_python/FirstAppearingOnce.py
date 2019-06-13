# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.s = ''
        self.table = [0 for _ in range(255)]

    def FirstAppearingOnce(self):
        # write code here
        for c in self.s:
            if self.table[ord(c)] == 1:
                return c
        return '#'

    def Insert(self, char):
        # write code here
        self.s += char
        self.table[ord(char)] += 1
