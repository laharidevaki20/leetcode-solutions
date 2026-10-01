class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        result=[]
        for i in range(len(digits)):
            result.append(str(digits[i]))
        joined="".join(result)
        num=int(joined)+1
        num1=str(num)
        result2=[]
        for i in num1:
            result2.append(int(i))
        return result2
