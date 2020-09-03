class Solution(object):
    def createTargetArray(self, nums, index):
        target=[]
        for i in range(len(index)):
            target.insert(index[i],nums[i])
        return target

obj=Solution()
obj.createTargetArray([0,1,2,3,4],[0,1,2,2,1])