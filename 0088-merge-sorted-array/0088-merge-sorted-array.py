class Solution:
    def merge(self, nums1, m, nums2, n):
        p, i, j = m+n-1, m-1, n-1
        while j >= 0 and i >= 0:
            if nums1[i] >= nums2[j]:
                nums1[p] = nums1[i]
                i -= 1
            else:
                nums1[p] = nums2[j]
                j -= 1
            p -= 1
        while j >= 0:
            nums1[p] = nums2[j]
            j -= 1
            p -= 1