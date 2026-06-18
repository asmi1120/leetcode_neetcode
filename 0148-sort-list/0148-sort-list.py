# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        temp=head
        while temp!=None :
            arr.append(temp.val)
            temp=temp.next
        arr=sorted(arr)
        temp=head
        i=0
        while temp!=None:
            temp.val=arr[i]
            i+=1
            temp=temp.next
        return head
