# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        result=0 #5
        index=len(head)-1  #2
        for i in (head):
            result1=(2**index)*i #4
            index=index-1
            result+=result1
        return result

obj=Solution()
obj.getDecimalValue([1,0,0,0,0,1])