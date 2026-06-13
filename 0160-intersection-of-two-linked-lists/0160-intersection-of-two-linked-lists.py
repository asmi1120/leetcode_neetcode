# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None           
        i = headA
        j = headB
        while i != j:
            i = headB if i is None else i.next
            j = headA if j is None else j.next
        return i