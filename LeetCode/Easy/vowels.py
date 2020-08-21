class Solution(object):
    def removeVowels(self, s):
        s = s.replace("a","")
        s = s.replace("e","")
        s = s.replace("i","")
        s = s.replace("o","")
        s = s.replace("u","")
        return s
ob1 = Solution()
print(ob1.removeVowels("leetcodeisacommunityforcoders"))