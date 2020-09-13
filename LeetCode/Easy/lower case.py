class Solution(object):
    def toLowerCase(self, str):
        new=[]
        for i in str:
            if i.isupper():
                new.append(chr(ord(i)+32))
            else:
                new.append(i)
        joined=("".join(new))
        return(joined)
obj=Solution()
obj.toLowerCase("Hello")