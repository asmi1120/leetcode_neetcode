# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        prev,curr=dummy,head
        while curr!=None and curr.next!=None:
            nxtpairs=curr.next.next
            snd=curr.next
            snd.next=curr
            curr.next=nxtpairs
            prev.next=snd
            prev=curr
            curr=nxtpairs
        return dummy.next