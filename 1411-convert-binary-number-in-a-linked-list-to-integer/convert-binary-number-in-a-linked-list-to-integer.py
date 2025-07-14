# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        myS = ''
        n = head
        while n:
            myS += str(n.val)
            n = n.next
        
        print(myS)
        return int(myS, 2)
        