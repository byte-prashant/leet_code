# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:

        prev = ListNode()

        node = head
        prev = new_head=ListNode(0)
        prev.next = head
        while node and node.next:
            tail = node.next
            remaining = tail.next
            tail.next = node
            node.next = remaining
            prev.next = tail
            prev = node
            node = node.next

        return new_head.next
        
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        curr = head
        for _ in range(2):
            if not curr: return head
            curr = curr.next
		        
				
        # Reverse the group (basic way to reverse linked list)
        prev = None
        curr = head
        for _ in range(2):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
		
        # After reverse, we know that `head` is the tail of the group.
		# And `curr` is the next pointer in original linked list order
        head.next = self.swapPairs(curr)
        return prev