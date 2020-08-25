class Solution(object):
    def isPalindrome(self, x):
        return str(x)== str(x)[::-1]
obj=Solution()
obj.isPalindrome(10)