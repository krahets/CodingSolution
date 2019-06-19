import heapq
# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if not k or k > len(tinput): return []
        heap, res = [], []
        for n in tinput:
            if len(heap) < k:
                heapq.heappush(heap, -n)
            elif -n > heap[0]:
                heapq.heappush(heap, -n)
                heapq.heappop(heap)
        while heap:
            res.append(-heapq.heappop(heap))
        res.reverse()
        return res