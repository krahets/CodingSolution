# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        num_xor = array[0]
        for a in array[1:]:
            num_xor ^= a
        index = 0
        while num_xor & 1 != 1:
            num_xor >>= 1
            index += 1
        n0, n1 = 0, 0
        for a in array:
            if a >> index & 1: n0 ^= a
            else: n1 ^= a
        return [n0,n1]
    
s = Solution()
print(s.FindNumsAppearOnce([8,3,1,4,8,4,6,3,1,5,5,9]))