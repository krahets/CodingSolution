# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        tmp = list(numbers) # copy the list
        i = 1
        while i < len(tmp):
            if tmp[0] == tmp[i]:
                i += 1
            else:
                del tmp[0], tmp[i-1]
                i = 1
        if not tmp: return 0
        count = 0
        for num in numbers:
            if num == tmp[0]: count += 2
        return tmp[0] if count > len(numbers) else 0



s = Solution()
print(s.MoreThanHalfNum_Solution([1,2,3,4,4]))