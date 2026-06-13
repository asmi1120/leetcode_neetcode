# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        curr = head
        count = 1
        while curr is not None:
            curr = curr.next
            count += 1
        if count%2==0:
            mid =(count//2)-1
        else:
            mid=count//2
        curr = head
        for _ in range(mid):
            curr = curr.next
            
        return curr

