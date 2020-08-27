class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        greatest = max(candies)  # 5
        result = []
        for i in candies:
            if (i + extraCandies) >= greatest:
                result.append(True)
            else:
                result.append(False)

        return result


obj = Solution()
obj.kidsWithCandies([12, 1, 12], 1)