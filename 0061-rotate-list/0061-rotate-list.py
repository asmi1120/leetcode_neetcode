# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None:
            return None
        count=0
        curr=head
        while curr!=None:
            curr=curr.next
            count+=1
        if count==1:
            return head
        k=k%count
        curr=head
        prev=curr
        while k>0:
            while curr!=None and curr.next!=None:
                prev=curr
                curr=curr.next
            prev.next.next=head
            prev.next=None
            head=curr
            k-=1
        return head


        