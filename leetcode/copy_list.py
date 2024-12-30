class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        seen = {}
        newHead = None
        curr = head
        while curr != None:
            newNode = Node(curr.val)
            seen[curr] = newNode
            curr = curr.next
        
        curr = head
        while curr != None:
            copy_node = seen[curr]
            if newHead == None:
                newHead = copy_node
            original_next = curr.next if curr.next else None
            original_rp = curr.random if curr.random else None

            copy_node_next = None if original_next == None else seen[original_next]
            copy_node_random = None if original_rp == None else seen[original_rp]

            

            copy_node.next = copy_node_next
            copy_node.random = copy_node_random

            curr = curr.next

        return newHead
