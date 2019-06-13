# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.que, self.asi = [], []
    def push(self, node):
        # write code here
        self.que.append(node)
    def pop(self):
        # return xx
        if not self.asi:
            if not self.que: return
            while self.que:
                self.asi.append(self.que.pop())
        return self.asi.pop()