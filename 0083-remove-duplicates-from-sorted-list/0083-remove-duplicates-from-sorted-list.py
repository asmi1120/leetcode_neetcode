# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        visited = set()
        curr = head
        visited.add(curr.val)
        while curr.next is not None:
            if curr.next.val in visited:
                curr.next = curr.next.next
            else:
                visited.add(curr.next.val)
                curr = curr.next
        return head
        