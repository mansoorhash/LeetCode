# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)

        behind = dummy
        ahead = dummy
        for _ in range(n-1):
            ahead = ahead.next
        while ahead.next != None:
            ahead = ahead.next
            if ahead.next == None:
                behind.next = behind.next.next
            else:
                behind = behind.next
        return dummy.next
