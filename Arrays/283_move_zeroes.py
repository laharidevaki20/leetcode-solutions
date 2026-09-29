class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        zero=[]
        non_zero=[]
        for i in range(0,len(nums)):
            if nums[i] == 0:
                zero.append(nums[i])
            else:
                non_zero.append(nums[i])
        non_zero.extend(zero)
        for i in range(0,len(nums)):
            nums[i] = non_zero[i]
        print(non_zero)