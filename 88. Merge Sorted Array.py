# 88. Merge Sorted Array

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i=m-1
        j=n-1
        l=m+n-1

        while(j>=0):
            if i>=0 and nums1[i]>nums2[j]:
                nums1[l]=nums1[i]
                i-=1
            else:
                nums1[l]=nums2[j]
                j-=1
                
            l-=1
            
