class Solution(object):
    def xorOperation(self, n, start):
        a=start #0
        if n==0 or n==1:
            return start
        for i in range(start+2,(start+(2*n)),2):
            res=a^i
            a,i=res,i+2
        return res
obj=Solution()
obj.xorOperation(10,5)