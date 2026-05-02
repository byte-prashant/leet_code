# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 12345 =>4
        # 
        prev=None
        org_head= head
        nth = head
        count = 0
        n= n-1
        while(head and head.next):
            
            if count>=n:
                prev = nth
                nth = nth.next
            head = head.next
            count+=1
        
        if prev:
                print(prev.val,nth.val,head.val)
                prev.next = nth.next
                head = org_head
        else:
            head = nth.next
        

        return head

                
        