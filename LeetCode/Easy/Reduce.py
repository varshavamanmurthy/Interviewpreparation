class Solution(object):
    def numberOfSteps(self, num):
        count = 0
        while num != 0:
            if num % 2 == 0:
                num = num // 2  # 4
                count += 1
                continue
            else:
                num = num - 1
                count += 1
                continue

        return count


obj = Solution()
obj.numberOfSteps(14)