# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy     
        
        while pre.next !=None and pre.next.next !=None:
            
            node1 = pre.next
            node2 = node1.next
            last = node2.next
            
            pre.next = node2
            node2.next = node1
            node1.next = last
            
            pre = node1
        
        return dummy.next
            
