# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        prev, curr = dummy, head
        while curr and curr.next:
            future = curr.next.next
            last = curr.next

            last.next = curr
            curr.next = future

            prev.next = last

            prev = curr
            curr = future

        return dummy.next