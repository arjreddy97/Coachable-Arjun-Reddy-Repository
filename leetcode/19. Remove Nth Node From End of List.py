# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head.next == None:
            if n == 1:
                return None
            return head
        
        counter = 1
        second = head
        while counter <= n:
            second = second.next
            counter += 1
        
        if second == None:
            head.val = head.next.val
            head.next = head.next.next
            return head
        
        
        first = head
        
