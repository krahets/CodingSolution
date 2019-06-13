import heapq
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.q = []
        self.p = []
    def Insert(self, num):
        # write code here
        if not self.p or num <= -self.p[0]: heapq.heappush(self.p, -num)
        else: heapq.heappush(self.q, num)
        if len(self.p) == len(self.q) + 2: heapq.heappush(self.q, -heapq.heappop(self.p))
        if len(self.p) + 1 == len(self.q): heapq.heappush(self.p, -heapq.heappop(self.q))
    def GetMedian(self, data):
        # write code here
        return (self.q[-1] - self.p[-1]) / 2.0 if len(self.q) == len(self.p) else -self.p[-1]


s = Solution()
s.Insert(5)
print(s.q,s.p)
print(s.GetMedian([]))
s.Insert(2)
print(s.q,s.p)

print(s.GetMedian([]))
s.Insert(3)
print(s.q,s.p)

print(s.GetMedian([]))
s.Insert(4)
print(s.q,s.p)

print(s.GetMedian([]))
s.Insert(1)
print(s.q,s.p)

print(s.GetMedian([]))
s.Insert(6)
print(s.q,s.p)

print(s.GetMedian([]))
s.Insert(7)
print(s.q,s.p)

print(s.GetMedian([]))
s.Insert(0)
print(s.q,s.p)

print(s.GetMedian([]))
s.Insert(8)
print(s.q,s.p)

print(s.GetMedian([]))
