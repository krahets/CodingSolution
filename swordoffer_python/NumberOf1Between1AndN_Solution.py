# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        total, deno, count, end = 0, 1, 0, 0
        while n != 0:
            num = n % (deno * 10)
            n -= num
            if num > deno:
                count += total * num / deno + deno
            elif num == deno:
                count += total + 1 + end
            total = total*10 + deno
            end += num
            deno *= 10
        return int(count)

    def NumberOf1Between1AndN_Solution1(self, n):
        # write code here
        arr = [str(i) for i in range(1, n+1)]
        tmp = "".join(arr)
        res = 0
        for t in tmp:
            if t == '1':
                res += 1
        return res


s = Solution()
print(s.NumberOf1Between1AndN_Solution(11345))
print(s.NumberOf1Between1AndN_Solution1(11345))
