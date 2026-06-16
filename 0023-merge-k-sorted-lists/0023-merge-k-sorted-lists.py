# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
        head =ans = ListNode("head")
        heap =[]
        max_elem = 0
        all_list_traversed = len(lists)
        for idx,node in enumerate(lists):
            if node:
                heapq.heappush(heap,(node.val,idx,node))

        head = tail = ListNode("head")
        while heap:
           val, idx, node  = heapq.heappop(heap)
           print(val)
           tail.next = node
           tail = tail.next

           if node.next:
                heapq.heappush(heap,(node.next.val,idx,node.next))


                    

           
        return head.next






        

        


        
        