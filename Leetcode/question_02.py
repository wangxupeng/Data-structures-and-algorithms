# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        tmp = ListNode(0)#表头
        res = tmp
        carry = 0 
        
        while l1 or l2:
            node_value = 0
            if l1:
                node_value = l1.val 
                l1 = l1.next
            if l2:
                node_value += l2.val
                l2 = l2.next
            res.next = ListNode((node_value+ carry) % 10)
            res = res.next
            carry = (node_value+ carry) //10
            
        if carry == 1:
            res.next = ListNode(carry)
        res = tmp.next #除表头之外的链表
        del tmp
        return res

if __name__ == "__main__":
    t1 = ListNode(3)
    t2 = ListNode(4)
    t2.next = t1
    t3 = ListNode(2)
    t3.next = t2


    b1 = ListNode(4)
    b2 = ListNode(6)
    b2.next = b1
    b3 = ListNode(5)
    b3.next = b2

    result = Solution()
    add_sum = result.addTwoNumbers(t3, b3)

    while (add_sum != None):
        print (add_sum.val)
        add_sum = add_sum.next
                
                
                
                
                
