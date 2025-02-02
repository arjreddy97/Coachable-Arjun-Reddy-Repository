# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        p1 = l1
        p2 = l2
        dunny = None
        
        while p1 is not None and p2 is not None:
            if p1.val < p2.val:
                p1p = p1
                dummy = p1.next
                
            else:
                if dummy is not None:
                    p1p.next = p2
                dummy = p2
                p2 = p2.next
                dummy.next = p1
        
        if p1 is None:
            dummy.next = p2
        
        return l1 if l1.val < l2.val else l2
