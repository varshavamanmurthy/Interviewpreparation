class Solution(object):
    def defangIPaddr(self, address):
        return address.replace('.', '[.]')

obj = Solution()
obj.defangIPaddr("255.100.50.0")