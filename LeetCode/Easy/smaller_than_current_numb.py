class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        count=0
        res=[]
        for i in nums:
            for j in nums:
                if i > j and i!=j:
                    count+=1
            res.append(count)
            count=0
        return res
obj = Solution()
obj.smallerNumbersThanCurrent([8,1,2,2,3])
