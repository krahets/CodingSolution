class Solution:
    def maxChunksToSorted(self, arr: [int]) -> int:
        stack = []
        for num in arr:
            if stack and num < stack[-1]: 
                head = stack.pop()
                while stack and num < stack[-1]: stack.pop()
                stack.append(head)
            else: stack.append(num)
        return len(stack)
          


s = Solution()
print(s.maxChunksToSorted([1,1,2,1,1,3,4,5,3,6]))


