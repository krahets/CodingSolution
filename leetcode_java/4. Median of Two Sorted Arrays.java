class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        if(nums1.length > nums2.length) return findMedianSortedArrays(nums2, nums1);
        int l = 0, r = 2 * nums1.length;
        int m1, m2, left1 = 0, left2 = 0, right1 = 0, right2 = 0;
        while(l <= r) {
            m1 = (l + r) / 2;
            m2 = nums1.length + nums2.length - m1;
            left1 = m1 != 0 ? nums1[(m1 - 1) / 2] : Integer.MIN_VALUE;
            right1 = m1 != 2 * nums1.length ? nums1[m1 / 2] : Integer.MAX_VALUE;
            left2 = m2 != 0 ? nums2[(m2 - 1) / 2] : Integer.MIN_VALUE;
            right2 = m2 != 2 * nums2.length ? nums2[m2 / 2]: Integer.MAX_VALUE;
            if(left1 > right2) r = m1 - 1;
            else if(left2 > right1) l = m1 + 1;
            else break;
        }
        return (Math.max(left1, left2) + Math.min(right1, right2)) / 2.0;
    }
}