class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        sort_nums = sorted(nums1 + nums2)
        if len(sort_nums) % 2 == 0:
            middle = len(sort_nums) // 2
            return (sort_nums[middle] + sort_nums[middle-1])*1.0 / 2
        else:
            return sort_nums[(len(sort_nums) // 2)]
            
        
