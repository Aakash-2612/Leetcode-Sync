# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        def check(nums, val):
            if val in nums:
                return True
            else:
                return False

        cur = ListNode(None)
        s = set(nums)
        dummy = cur
        temp = head
        while temp:
            if not check(s, temp.val):
                cur.next = ListNode(temp.val)
                cur = cur.next
            temp = temp.next
        return dummy.next