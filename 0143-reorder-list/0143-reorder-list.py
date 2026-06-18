# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow=head
        fast=head.next
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        snd=slow.next
        prev=slow.next=None
        while snd!=None:
            tmp=snd.next
            snd.next=prev
            prev=snd
            snd=tmp
        first,second=head,prev
        while second!=None:
            tmp1,tmp2=first.next,second.next
            first.next=second
            second.next=tmp1
            first=tmp1
            second=tmp2

        