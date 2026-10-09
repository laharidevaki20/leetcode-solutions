class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result=[]
        for i in set(nums1):
            if i in nums2:
                result.append(i)
        return result