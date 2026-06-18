# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s=self.rev(l1)
        r=self.rev(l2)
        left=ListNode()
        n=left
        v=0
        while s!=None or r!=None or v:
            val1 = s.val if s else 0
            val2 = r.val if r else 0
            total = val1 + val2 + v
            v = total // 10
            n.next = ListNode(total % 10)  
            n = n.next
            s = s.next if s else None
            r = r.next if r else None
        m=self.rev(left.next)
        return m
    def rev(self,head):
        prev=None
        slow=head
        while slow!=None:
            tmp=slow.next
            slow.next=prev
            prev=slow
            slow=tmp
        return prev