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


    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def print_linked_list(head):
            print("------linked list")
            nums = []
            while head:
                nums.append(head.val)
                head = head.next
            print(nums)

        def mutate_list():
            dummy = ListNode(None, head)
            count = 0
            left= 0
            ptr = head
            ktail = dummy
            while ptr:

                c = left
                while ptr and c<left+k:
                    ptr=ptr.next
                    c+=1

                if not c  == left+k:
                    break
                curr = ktail.next
                for i in range(left+k-left-1):
                    #print_linked_list(dummy)
                    node_to_move = curr.next
                    curr.next = node_to_move.next
                    node_to_move.next = ktail.next
                    ktail.next = node_to_move

                ktail = curr
               
                left= left+k
            return dummy.next

        return mutate_list()


    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        for _ in range(k):
            if not curr: return head
            curr = curr.next
		        
				
        # Reverse the group (basic way to reverse linked list)
        prev = None
        curr = head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
		
        # After reverse, we know that `head` is the tail of the group.
		# And `curr` is the next pointer in original linked list order
        head.next = self.reverseKGroup(curr, k)
        return prev

            

            

        