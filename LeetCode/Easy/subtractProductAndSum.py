class Solution(object):
    def subtractProductAndSum(self, n):
        product=1
        summ=0
        for i in str(n):
            product*=int(i)
            summ+=int(i)
        return product-summ
obj = Solution()
obj.subtractProductAndSum(234)