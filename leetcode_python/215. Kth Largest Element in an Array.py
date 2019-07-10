import heapq
class Solution:
    def findKthLargest(self, nums: [int], k: int) -> int:
        heap = []
        for num in nums[:k]:
            heapq.heappush(heap, num)
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
        return heap[0]