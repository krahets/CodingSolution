# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        self.quick_sort(numbers, 0, len(numbers)-1)
        return "".join([str(num) for num in numbers])

    def quick_sort(self, arr, l, r):
        if l > r:
            return
        base, i, j = arr[l], l, r
        while i != j:
            while self.compare(arr[j], base) and i < j:
                j -= 1
            while self.compare(base, arr[i]) and i < j:
                i += 1
            arr[i], arr[j] = arr[j], arr[i]
        arr[l], arr[i] = arr[i], arr[l]
        self.quick_sort(arr, l, i-1)
        self.quick_sort(arr, i+1, r)

    def compare(self, a, b):
        str1, str2 = str(a) + str(b), str(b) + str(a)
        return 0 if str1 < str2 else 1


s = Solution()
print(s.PrintMinNumber([3, 32, 321, 25, 23]))
