class Solution(object):
    def balancedStringSplit(self, s):
        count = 0
        ans = 0
        for S in s:
            if (S == 'R'):
                count += 1
            else:
                count -= 1
            if (count == 0):
                ans += 1
        return ans


obj = Solution()
obj.balancedStringSplit("RLRRLLRLRL")