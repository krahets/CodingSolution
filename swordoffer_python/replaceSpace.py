# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        l = list(s)
        count = 0
        for k in l:
            if k == ' ':
                count+=1
                l.extend(['1','1'])
        for i in range(len(s)-1,-1,-1):
            if l[i]!=' ':
                l[i+2*count]=l[i]
            else:
                count-=1 
                l[i+2*count]='%'
                l[i+2*count+1]='2'
                l[i+2*count+2]='0'
        return ''.join(l)