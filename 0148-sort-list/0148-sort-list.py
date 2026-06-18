# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        middle=self.mid(head)
        leftnode=head
        rightnode=middle.next
        middle.next=None
        leftnode=self.sortList(leftnode)
        rightnode=self.sortList(rightnode)
        return self.sortfn(leftnode,rightnode)
    def sortfn(self,leftnode,rightnode):
        cur = dummy = ListNode()
        while leftnode and rightnode:               
            if leftnode.val < rightnode.val:
                cur.next = leftnode
                leftnode, cur = leftnode.next, leftnode
            else:
                cur.next = rightnode
                rightnode, cur = rightnode.next, rightnode
                
        if leftnode or rightnode:
            cur.next = leftnode if leftnode else rightnode    
        return dummy.next
    def mid(self,head):
        slow=head
        fast=head.next
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        return slow