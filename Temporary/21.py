# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        point = root = ListNode(0)
        while l1 or l2:
            if l1 and l2:
                if l1.val<l2.val:
                    point.next = ListNode(l1.val)
                    l1=l1.next
                else:
                    point.next = ListNode(l2.val)
                    l2=l2.next
            elif l1:
                point.next = ListNode(l1.val)
                l1=l1.next
            else:
                point.next = ListNode(l2.val)
                l2=l2.next
            point = point.next
        return root.next
