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
        root = ListNode(0)
        l3 = root
        carryValue = 0
        while l1!=None or l2!=None or carryValue==1:
            sumValue=carryValue
            if l1!=None:
                sumValue += l1.val
                l1 = l1.next
            if l2!=None:
                sumValue += l2.val
                l2 = l2.next        
            if sumValue >= 10:
                carryValue = 1
                sumValue = sumValue -10
            else:
                carryValue = 0
            l3.next = ListNode(sumValue)
            l3 = l3.next
        return root.next