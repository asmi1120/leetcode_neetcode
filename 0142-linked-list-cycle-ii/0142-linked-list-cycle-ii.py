# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next==None:
            return None
        slow=head
        fast=head
        s=1
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
            s+=1
            if slow==fast:
                break
        else: return None
        while head != slow:
            head= head.next
            slow=slow.next
        return head