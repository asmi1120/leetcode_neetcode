# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left,right=ListNode(),ListNode()
        il,ir=left,right
        temp=head
        while temp!=None:
            if temp.val<x:
                il.next=temp
                il=il.next
            else:
                ir.next=temp
                ir=ir.next
            temp=temp.next
        il.next=right.next
        ir.next=None
        return left.next
        