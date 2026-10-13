class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        pos=[]
        neg=[]
        for i in range (0,len(nums)):
            if nums[i] > 0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        k=0
        for i in range(len(pos)):
            nums[k] = pos[i]
            k += 1
            nums[k] = neg[i]
            k += 1
        return nums