# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def recurseList(self, node):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if node.next == None:
            self.head = self.current = ListNode(node.val)
        else:
            self.recurseList(node.next)
            self.current.next = ListNode(node.val)
            self.current = self.current.next

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        self.recurseList(head)
        return self.head
