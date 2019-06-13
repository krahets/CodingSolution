# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        numbers.sort()
        joker = 0
        for n in numbers[:4]:
            if not n: joker += 1
        for i in range(joker, len(numbers) - 1):
            tmp = numbers[i+1] - numbers[i] - 1
            joker -= tmp
            if joker < 0 or tmp < 0: return False
        return True if numbers else False


s = Solution()
print(s.IsContinuous([1,0,0,5,0]))
