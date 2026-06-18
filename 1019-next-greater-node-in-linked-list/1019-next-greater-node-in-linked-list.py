# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        prev=None
        slow=head
        count=0
        while slow!=None:
            tmp=slow.next
            slow.next=prev
            prev=slow
            slow=tmp
            count+=1
        tmp=prev
        s=[]
        ans=[0]*count
        i=0
        while tmp!=None:
            while s and s[-1]<=tmp.val:
                s.pop()
            ans[i]=s[-1] if s else 0
            s.append(tmp.val)
            tmp=tmp.next
            i+=1
        return ans[::-1]
