# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        new_head = ListNode(head, None)

        def reverse_list(head_node, size):
            prev_node, curr = None, head_node
            while size:
                next_node = curr.next
                curr.next = prev_node
                prev_node = curr
                curr = next_node
                size-=1
            return prev_node


        ptr = current_node =  head
        ktail  = new_head

        while ptr:
            count = 0

            ptr = current_node
            while count<k and ptr:
                ptr = ptr.next
                count+=1

            if count == k:

                rev_head = reverse_list(current_node, k)

                
                ktail.next = rev_head
                ktail = current_node
                current_node = ptr

        #print("--------",ktail.val, current_node.val)
        ktail.next = current_node
        
        return new_head.next



            

            

        