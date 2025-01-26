"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        createClones(head)
        populateRandomPointers(head)
        return getClonedList(head)
        
def getClonedList(head):
    if not head:
        return 
    current = head
    newListHead = current.next
    while current.next is not None:
        nextNode = current.next
        current.next = current.next.next
        current = nextNode
    return newListHead
        
        
def populateRandomPointers(head):
    current = head
    while current is not None:
        current.next.random = None if current.random is None else current.random.next
        current = current.next.next
    
def createClones(head):
    current = head
    while current is not None:
        nextNode = current.next
        clone = Node(current.val)
        current.next = clone
        clone.next = nextNode
        current = nextNode
    
        

    
