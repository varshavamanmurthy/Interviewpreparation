class Solution(object):
    def restoreString(self, s, indices):
        result=''
        a=list(sorted((zip(indices,s))))
        for k,v in a:
            result+=v
        return result
obj=Solution()
obj.restoreString("abc",[0,1,2])