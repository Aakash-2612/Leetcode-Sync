# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = ''
        b = ''
        cur = l1
        while cur:
            a += str(cur.val)
            cur = cur.next
        a = int(a[::-1])
        cur2 = l2
        while cur2:
            b += str(cur2.val)
            cur2 = cur2.next
        b = int(b[::-1])
        ans = str(a+b)
        print(ans)
        head = None
        for i in ans:
            newnode = ListNode(int(i))
            if head is None:
                head = newnode
            else:
                newnode.next = head
                head = newnode

        return head