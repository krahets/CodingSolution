# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        tmp = list(numbers)
        i = 1
        while i < len(tmp):
            if tmp[0] != tmp[i]:
                del tmp[i], tmp[0]
                i = 1
            else:
                i += 1
        if not tmp:
            return 0
        k = 0
        for num in numbers:
            if tmp[0] == num:
                k += 1
        return tmp[0] if 2 * k > len(numbers) else 0


s = Solution()
print(s.MoreThanHalfNum_Solution([1, 2, 3, 2, 2, 2, 5, 2, 3]))
