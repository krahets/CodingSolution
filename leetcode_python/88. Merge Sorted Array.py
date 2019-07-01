class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        tail, i, j = m + n - 1, m - 1, n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[tail] = nums1[i]
                i -= 1
            else:
                nums1[tail] = nums2[j]
                j -= 1
            tail -= 1
        for k in range(j, -1, -1): nums1[k] = nums2[k]