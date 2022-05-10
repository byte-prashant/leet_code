class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def reverseL(node):

            if not node:
                return node, None

            if not node.next:
                head, node = node, node
                return head, node

            head, new_node = reverseL(node.next)

            new_node.next = node
            node.next = None

            return head, node

        return reverseL(head)[0]
