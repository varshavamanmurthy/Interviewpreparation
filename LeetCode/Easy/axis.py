class Solution(object):
    def shuffle(self, nums, n):
        op = []
        for i in range(len(nums) // 2):
            op.append(nums[i])
            op.append(nums[i + n])
        return op
