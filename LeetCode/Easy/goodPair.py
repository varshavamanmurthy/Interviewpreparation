class Solution(object):
    def numIdenticalPairs(self, nums):
        count = 0
        for i in range(len(nums) - 1):
            for j in range(1, len(nums)):
                if nums[i] == nums[j] and i < j:
                    count += 1
        return count


obj = Solution()
obj.numIdenticalPairs([1, 2, 3])