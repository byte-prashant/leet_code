class Node:
    val =None
    next = None
    prev = None
    def __init__(self,val,key,prev=None, next=None):
        self.val = val
        self.next = next
        self.prev = prev
        self.key= key


class LRUCache:


    def __init__(self, capacity: int):
        self.hash_map = {}
        self.head = Node("head","head")
        self.tail = Node("tail","head")
        self.head.next = self.tail
        self.tail.prev= self.head
        self.capacity  = capacity


    def remove_node(self, node):
        next_node = node.next
        prev_node = node.prev
        prev_node.next = next_node
        next_node.prev = prev_node
       
        #self.print_list("delete")

        return 

    def add_to_front(self, new_node):
        next_node = self.head.next
        next_node.prev= new_node
        new_node.next = next_node
        self.head.next = new_node
        new_node.prev = self.head

        return

    def print_list(self,method):
        print("-----------------",method)
        head = self.head
        result = []
        while(head.next):
            result.append(head.key)
            head = head.next


        print(result)
        

    def get(self, key: int) -> int:
        if key in self.hash_map:
            node = self.hash_map.get(key)
            if node:
                self.remove_node(node)
                self.add_to_front(node)
            return node.val
        #self.print_list("get")
        return -1


        
        

    def put(self, key: int, value: int) -> None:
        new_node = Node(value, key)

        if key in self.hash_map:
            
            new_node = self.hash_map[key]
            self.remove_node(new_node)
            new_node.val = value
            self.add_to_front(new_node)

        elif len(self.hash_map)== self.capacity :
            #print("eviction-----",len(self.hash_map)-1)
            # delete the element
            node = self.tail.prev
            self.remove_node(node)
            del self.hash_map[node.key]
            self.add_to_front(new_node)
            self.hash_map[key] = new_node

        else :
            self.add_to_front(new_node)
            self.hash_map[key] = new_node

        #self.print_list("put")











# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)