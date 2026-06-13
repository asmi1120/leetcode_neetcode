# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        curr = head
        count = 0
        while curr is not None:
            curr = curr.next
            count += 1
        if n == count:
            return head.next
        curr=head
        c=1
        while curr is not None and c < count-n:
            curr = curr.next
            c += 1
        if curr is None or curr.next is None:
            return head
            
        curr.next = curr.next.next
        
        return head