# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.m_stack = []
    def push(self, node):
        # write code here
        self.stack.append(node)
        if not self.m_stack or self.m_stack[-1] >= node:
            self.m_stack.append(node)
    def pop(self):
        # write code here
        if self.stack.pop() == self.m_stack[-1]:
            self.m_stack.pop()
    def top(self):
        # write code here
        return self.stack[-1]
    def min(self):
        # write code here
        return self.m_stack[-1]
