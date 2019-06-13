class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        row = len(array)-1
        col = 0
        while row>=0 and col<len(array[0]):
            if target == array[row][col]:
                return True
            elif target > array[row][col]:
                col+=1
            else:
                row-=1
        return False