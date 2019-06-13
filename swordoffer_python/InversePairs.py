# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # write code here
        self.arr, self.count = data, 0
        self.merge_sort(0, len(data)-1)
        return self.count % 1000000007
    def merge_sort(self, l, r):
        if l >= r: return
        m = int((l+r+1)/2)
        self.merge_sort(l, m-1)
        self.merge_sort(m, r)
        i, j, merge = l, m, []
        while i < m and j <= r:
            if self.arr[i] < self.arr[j]:
                merge.append(self.arr[i])
                i += 1
            else:
                merge.append(self.arr[j])
                j += 1
                self.count += m - i
        for x in range(j,r+1): merge.append(self.arr[x])
        for x in range(i,m): merge.append(self.arr[x])
        for i in range(l, r+1): self.arr[i] = merge[i-l]
                


s = Solution()
s.InversePairs([3,3,1])
