# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root = point = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            x = 0
            if l1:
                x += l1.val
            if l2:
                x += l2.val
            x += carry
            point.next = ListNode(x%10)
            carry = x/10
            point = point.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return root.next
