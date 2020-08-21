class Solution(object):
    def runningSum(self, nums):
        output=[]
        summ=0
        for i in nums:
            summ+=i
            output.append(summ)
        return output

sol = Solution()
print(sol.runningSum([1,2,3,4]))