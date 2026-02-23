# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next == None: return head
        prev = None
        curr = head
        next_pos = head.next

        while next_pos:
            next_pos = curr.next
            curr.next = prev
            prev = curr
            curr = next_pos


        return prev
