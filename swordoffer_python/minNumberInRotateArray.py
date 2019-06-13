# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        left = 0
        right = len(rotateArray)-1
        while True:
            if right-left == 1:
                return rotateArray[right]
            mid = int((left+right)/2)
            if rotateArray[mid] == rotateArray[right] and rotateArray[mid] == rotateArray[left]:
                return minByOrder(rotateArray(left, right))
            elif rotateArray[mid] >= rotateArray[left]:
                left = mid
            else:
                right = mid

    def minByOrder(rotateArray):
        for i in range(len(rotateArray)-1, 0, -1):
            if rotateArray[i-1] > rotateArray[i]:
                return rotateArray[i]
        return rotateArray[0]