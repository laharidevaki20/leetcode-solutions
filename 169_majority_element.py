class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n=len(nums)
        count={}
        for i in nums:
            if i not in count:
                count[i]=1
            else:
                count[i]=count[i]+1
            if count[i] > n/2:
                return i
                